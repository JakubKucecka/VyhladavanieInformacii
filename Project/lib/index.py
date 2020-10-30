import gzip
import os
from whoosh.qparser import QueryParser, SimpleParser
from whoosh.analysis import SimpleAnalyzer
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID, STORED

from lib import handler


def index(index_dir_actor, index_dir_film, actor_file, film_file):
    print("\trun index...")
    schema = Schema(names=TEXT(stored=True, analyzer=SimpleAnalyzer(expression=r"[\w,.'\-_ ]+")), data=STORED,
                    films=STORED)
    if not os.path.exists(index_dir_actor):
        os.mkdir(index_dir_actor)

    ix = create_in(index_dir_actor, schema)
    writer_actor = ix.writer()

    with gzip.open(actor_file, 'rb') as f:
        count = 0

        for line in f:
            decode_line = line.decode("utf-8")
            count += 1

            array_line = handler.return_array(decode_line)
            names = array_line[0].split('\t') if array_line[0] != "NONE" else []
            aliases = array_line[1].split('\t') if array_line[1] != "NONE" else []
            writer_actor.add_document(names="\t".join(names + aliases),
                                      data=array_line[2:4],
                                      films=array_line[4:])

    print("\t\trun write index actor...")
    writer_actor.commit()
    del writer_actor

    schema = Schema(id=ID(stored=True), names=STORED)
    if not os.path.exists(index_dir_film):
        os.mkdir(index_dir_film)

    ix = create_in(index_dir_film, schema)
    writer_film = ix.writer()

    with gzip.open(film_file, 'rb') as f:
        count = 0

        for line in f:
            decode_line = line.decode("utf-8")
            count += 1

            array_line = handler.return_array(decode_line)
            writer_film.add_document(id=array_line[0], names=array_line[1])

    print("\t\trun write index film...")
    writer_film.commit()
    del writer_film


def search_actor(index_dir_actor, query_str):
    ix = open_dir(index_dir_actor)
    actors_array = []
    i = 0
    cmd = ''

    with ix.searcher() as searcher:
        query = QueryParser("names", ix.schema).parse('"' + query_str + '"')

        results = searcher.search(query, terms=True)

        if len(results) != 0:
            if len(results) > 1:
                print("I find more then one " + query_str + ", didn't you mean?")
                j = 1
                for r in results:
                    actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                         'query': str(query)[str(query).index(":") + 1:]})
                    names = r['names'].split('\t')
                    print("\t[" + str(j) + "] " + str(query)[str(query).index(":") + 1:] + " -> "
                          + ", ".join(names) + " -> born: " + r['data'][0] + " died: " + r['data'][1])
                    j += 1

                cmd = input("Enter num of actor or 'e' for end: ")
            else:
                for r in results:
                    actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                         'query': str(query)[str(query).index(":") + 1:]})
        else:
            corrected = searcher.correct_query(query, query_str)

            if corrected.query != query:
                results = searcher.search(corrected.query, terms=True)
                if len(results) != 0:
                    print("I didn't find " + query_str + ", didn't you mean?")
                    j = 1
                    for r in results:
                        actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                             'query': str(query)[str(query).index(":") + 1:]})
                        names = r['names'].split('\t')
                        print("\t[" + str(j) + "] " + str(query)[str(query).index(":") + 1:] + " -> "
                              + ", ".join(names) + " -> born: " + r['data'][0] + " died: " + r['data'][1])
                        j += 1

                    cmd = input("Enter num of actor or 'e' for end: ")
                else:
                    return -1

    if cmd == "e":
        return -2
    else:
        if cmd:
            i = int(cmd) - 1
        return actors_array[i]


def search_film(index_dir_film, query_str):
    ix = open_dir(index_dir_film)
    films_array = []

    with ix.searcher() as searcher:
        query = SimpleParser("id", ix.schema).parse(query_str)

        results = searcher.search(query, terms=True, limit=100)

        for r in results:
            films_array.append(r['names'])

    return films_array
