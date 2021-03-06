import gzip
import os
from whoosh.qparser import QueryParser
from whoosh.analysis import SimpleAnalyzer
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, STORED
from lib import handler

"""
file indexing function

input:
  the path to the file where the index is stored and the path to the file to the final damp

output:
  deleted variable and index written in file
"""


def index(index_dir, final_file):
    print("\trun index...")
    analyzer = SimpleAnalyzer(expression=r"[\w,.\"\\\-:\'_ ]+")
    schema = Schema(names=TEXT(stored=True), data=STORED,
                    films=TEXT(stored=True, analyzer=analyzer))
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    ix = create_in(index_dir, schema)
    writer_actor = ix.writer()

    with gzip.open(final_file, 'rb') as f:
        count = 0

        for line in f:
            decode_line = line.decode("utf-8")
            count += 1

            array_line = handler.return_array(decode_line)
            names = array_line[0].split('\t') if array_line[0] != "NONE" else []
            aliases = array_line[1].split('\t') if array_line[1] != "NONE" else []
            writer_actor.add_document(names="\t".join(names + aliases),
                                      data=array_line[2:4],
                                      films="@".join(array_line[4:]))

    print("\t\twrite index...")
    writer_actor.commit()
    del writer_actor


"""
The feature searches for actors and their movies

input:
  index path and input string to search for

output:
  list of films for the actor
"""


def search_actor(index_dir, query_str):
    ix = open_dir(index_dir)
    actors_array = []
    i = 0
    cmd = '0'

    with ix.searcher() as searcher:
        query = QueryParser("names", ix.schema).parse(query_str)

        results = searcher.search(query, terms=True)

        if len(results) != 0:
            if len(results) > 1:
                print("I find more then one " + query_str + ", didn't you mean?")
                j = 1
                for r in results:
                    query_array = str(query).split('AND')
                    query_array_tmp = []
                    for q in query_array:
                        if len(query_array) == 1:
                            query_array_tmp.append(str(q)[str(q).index(":") + 1:])
                        else:
                            query_array_tmp.append(str(q)[str(q).index(":") + 1:-1])
                    query_tmp = " ".join(query_array_tmp)
                    actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                         'query': query_tmp})
                    names = r['names'].split('\t')
                    print("\t[" + str(j) + "] " + query_tmp + " -> "
                          + ", ".join(names) + " -> born: " + r['data'][0] + " died: " + r['data'][1])
                    j += 1

                cmd = input("Enter num of actor or 'e' for end: ")
            else:
                for r in results:
                    query_array = str(query).split('AND')
                    query_array_tmp = []
                    for q in query_array:
                        if len(query_array) == 1:
                            query_array_tmp.append(str(q)[str(q).index(":") + 1:])
                        else:
                            query_array_tmp.append(str(q)[str(q).index(":") + 1:-1])
                    query_tmp = " ".join(query_array_tmp)
                    actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                         'query': query_tmp})
        else:
            corrected = searcher.correct_query(query, query_str)

            if corrected.query != query:
                results = searcher.search(corrected.query, terms=True)
                if len(results) != 0:
                    print("I didn't find " + query_str + ", didn't you mean?")
                    j = 1
                    for r in results:
                        query_array = str(query).split('AND')
                        query_array_tmp = []
                        for q in query_array:
                            if len(query_array) == 1:
                                query_array_tmp.append(str(q)[str(q).index(":") + 1:])
                            else:
                                query_array_tmp.append(str(q)[str(q).index(":") + 1:-1])
                        query_tmp = " ".join(query_array_tmp)
                        actors_array.append({'names': r['names'], 'data': r['data'], 'films': r['films'],
                                             'query': query_tmp})
                        names = r['names'].split('\t')
                        print("\t[" + str(j) + "] " + query_tmp + " -> "
                              + ", ".join(names) + " -> born: " + r['data'][0] + " died: " + r['data'][1])
                        j += 1

                    cmd = input("Enter num of actor or 'e' for end: ")
                else:
                    print("Actor not found!")
                    return -1

    if not cmd.isdigit() or cmd == "e":
        print("Actor not found!")
        return -2
    else:
        if cmd:
            i = int(cmd) - 1
        if not len(actors_array):
            print("Actor not found!")
            return -1
        return actors_array[i]


"""
the function searches by movie title

input:
    path to the index and the entire string

output:
    a field of actors starring in a sought-after film
"""


def search_film(index_dir, query_str):
    ix = open_dir(index_dir)
    actors_array = []
    films_array = {}
    cmd = 'n'

    with ix.searcher() as searcher:
        query = QueryParser("films", ix.schema).parse('"' + query_str + '"')

        results = searcher.search(query, terms=True, limit=None)

        if len(results) != 0:
            for r in results:
                for films in r['films'].split('@'):
                    for f in films.split('\t'):
                        if str(query)[str(query).index(":") + 1:] == f.lower():
                            if films.split('\t')[0] not in films_array:
                                films_array[films.split('\t')[0]] = {'names': [r['names'].split('\t')[0]],
                                                                     'films': r['films']}
                            else:
                                films_array[films.split('\t')[0]]['names'].append(r['names'].split('\t')[0])
            if len(films_array) > 1:
                print("I find more then one " + query_str + ", didn't you mean?")
                j = 1
                for f in films_array.values():
                    film_string = ""
                    for film_list in f['films'].split('@'):
                        for film_from_list in film_list.split('\t'):
                            if str(query)[str(query).index(":") + 1:] == film_from_list.lower():
                                film_string = ", ".join(film_list.split('\t')[1:])
                    print("\t[" + str(j) + "] " + str(query)[str(query).index(":") + 1:] + " -> "
                          + film_string)
                    j += 1

                cmd = input("Enter num of movie or 'e' for end: ")
                if cmd == 'e' or not cmd.isdigit():
                    return -2
                else:
                    j = 0
                    for f in films_array.values():
                        if j == int(cmd) - 1:
                            actors_array = f['names']
                            break
                        j += 1

                    cmd = 'n'
            else:
                for f in films_array.values():
                    actors_array = f['names']
        else:
            corrected = searcher.correct_query(query, query_str)

            if corrected.query != query:
                cmd = input("I didn't find '" + query_str + "', didn't you mean '"
                            + str(corrected.query)[str(corrected.query).index(":") + 1:] + "'? [y|n]: ")
                if cmd == "y":
                    results = searcher.search(corrected.query, terms=True, limit=None)
                    if len(results) != 0:
                        for r in results:
                            for films in r['films'].split('@'):
                                for f in films.split('\t'):
                                    if str(corrected.query)[str(corrected.query).index(":") + 1:] == f.lower():
                                        if films.split('\t')[0] not in films_array:
                                            films_array[films.split('\t')[0]] = {'names': [r['names'].split('\t')[0]],
                                                                                 'films': r['films']}
                                        else:
                                            films_array[films.split('\t')[0]]['names'].append(r['names'].split('\t')[0])

                        if len(films_array) > 1:
                            print("I find more then one " + query_str + ", didn't you mean?")
                            j = 1
                            for f in films_array.values():
                                film_string = ""
                                for film_list in f['films'].split('@'):
                                    for film_from_list in film_list.split('\t'):
                                        if str(corrected.query)[
                                           str(corrected.query).index(":") + 1:] == film_from_list.lower():
                                            film_string = ", ".join(film_list.split('\t')[1:])
                                print("\t[" + str(j) + "] " + str(corrected.query)[
                                                              str(corrected.query).index(":") + 1:] + " -> "
                                      + film_string)
                                j += 1

                            cmd = input("Enter num of movie or 'e' for end: ")
                            if cmd == 'e' or not cmd.isdigit():
                                return -2
                            else:
                                j = 0
                                for f in films_array.values():
                                    if j == int(cmd) - 1:
                                        actors_array = f['names']
                                        break
                                    j += 1

                                cmd = 'n'
                        else:
                            for f in films_array.values():
                                actors_array = f['names']
                    else:
                        return -1
                elif cmd == "n":
                    print("Movie not found!")
                    return -1
                else:
                    print("Movie not found!")
                    return -2
            else:
                print("Movie not found!")
                return -1

    if cmd != "y" and cmd != "n":
        print("ERROR: Unknown input")
        exit(1)
    else:
        return actors_array
