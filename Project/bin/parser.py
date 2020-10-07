#!/usr/bin/env python3

from datetime import datetime
import gzip
import locale
import os
import re

locale.setlocale(locale.LC_ALL, '')

# input_file = input("Enter full path your file: ")
input_file = '../etc/film_dump_from_freebase_rdf.gz'
output_file_actors = "../etc/parse/actors.gz"
output_file_performances = "../etc/parse/performances.gz"
output_file_other = "../etc/parse/other.gz"
output_file_final = "../etc/parse/final.gz"


def return_first_column(input_line):
    tmp_line = re.split('[<>]', input_line)[1]
    return re.split('http://rdf.freebase.com/ns/', tmp_line)[1]


def return_id(input_line):
    tmp_line = re.split('[<>]', input_line)[5]
    return re.split('http://rdf.freebase.com/ns/', tmp_line)[1]


def return_name_or_date(input_line):
    tmp_line = re.split('[<>]', input_line)[4]
    return re.split('"', tmp_line)[1]


def return_array(input_line):
    tmp_array = re.split('[<>]', input_line)
    ret_array = []
    i = 0
    for item in tmp_array:
        if i % 2 == 1:
            ret_array.append(item)
        i += 1
    return ret_array


def open_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return gzip.open(file_name, "wt", encoding="utf-8", newline='')


def search():
    not_end = "y"

    while not_end == "y":
        print("\nrun SEARCH...")
        print("\trun search...")
        name1 = input("\nEnter first name: ")
        name2 = input("Enter second name: ")

        if name1.upper() == name2.upper():
            print("ERROR: Enter diferent names")
            continue

        with gzip.open(output_file_final, 'rb') as f:
            persons = []
            num_of_actors = 0

            for line in f:
                decode_line = line.decode("utf-8")
                array_line = return_array(decode_line)

                if array_line[0].upper() == name1.upper() or array_line[0].upper() == name2.upper():
                    con = 0
                    i = -1
                    for actor in persons:
                        i += 1
                        if array_line[0] == actor[0]:
                            con = 1
                            break

                    if con:
                        for j in array_line[4:]:
                            persons[i].append(j)
                    else:
                        array_line[3] = datetime.now().strftime("%Y-%m-%d") if array_line[3] == "NOW" else array_line[3]
                        persons.append(array_line)
                        num_of_actors += 1

            if num_of_actors < 2:
                print("ERROR: The actors " + name1 + " or " + name2 + " not found")
            else:
                if datetime.strptime(persons[0][2], '%Y-%m-%d') <= datetime.strptime(persons[1][3], '%Y-%m-%d') \
                        and datetime.strptime(persons[1][2], '%Y-%m-%d') <= datetime.strptime(persons[0][3], '%Y-%m-%d'):
                    films_array = []
                    for film_p1 in persons[0][4:]:
                        for film_p2 in persons[1][4:]:
                            if film_p1.upper() == film_p2.upper():
                                films_array.append(film_p1)

                    films = ','.join(films_array)
                    if films:
                        print("Actors " + name1 + " and " + name2 + " played together in films: " + films)
                    else:
                        print("ERROR: The actors " + name1 + " and " + name2 + " did not play together")
                else:
                    print("ERROR: The actors " + name1 + " and " + name2
                          + "  could not play together because they did not live at the same time")

        not_end = input("\nDo you want to continue? [y|n]: ")

    print("\nDONE")


cmd = input("You want to run a dump? [y|n]: ")
if cmd == "y":
    # print("run DUMP...")
    # with gzip.open(input_file, 'rb') as f:
    #     fa = open_file(output_file_actors)
    #     fp = open_file(output_file_performances)
    #     fo = open_file(output_file_other)
    #     count = 0
    #
    #     for line in f:
    #
    #         decode_line = line.decode("utf-8")
    #         count += 1
    #
    #         if re.search(
    #                 "^<http://rdf.freebase.com/ns/[m|g][.].*>[ ]*<http://rdf[.]freebase[.]com/ns/film[.]actor[.]film.*>[ ]*<.*>.*$",
    #                 decode_line):
    #             fa.write(decode_line)
    #         elif re.search(
    #                 "^<http://rdf.freebase.com/ns/[m|g][.].*>[ ]*<http://rdf[.]freebase[.]com/ns/film[.]performance[.]film.*>[ ]*<.*>.*$",
    #                 decode_line):
    #             fp.write(decode_line)
    #         elif re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line) \
    #                 or re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", decode_line) \
    #                 or re.search("<http://rdf[.]freebase[.]com/ns/people[.]person[.]date_of_birth>", decode_line) \
    #                 or re.search("<http://rdf[.]freebase[.]com/ns/people[.]deceased_person[.]date_of_death>", decode_line):
    #             fo.write(decode_line)
    #
    #         if count % 1000000 == 0:
    #             print("line: " + str(f'{count:n}') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")
    #
    #     print("line: " + str(f'{count: }') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")
    #     fa.close()
    #     fp.close()
    #     fo.close()

    print("\nrun PARSE...")
    ACTOR = {}
    PERF_FILM = {}
    FILM_ID_NAME = {}

    print("\trun parse actors...")
    with gzip.open(output_file_actors, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = return_first_column(decode_line)
            last_col = return_id(decode_line)
            if first_col not in ACTOR:
                ACTOR[first_col] = {'name': "", 'alias': "", 'b_date': "", 'd_date': "", 'films': {last_col: ""}}
            if first_col in ACTOR and last_col not in ACTOR[first_col]['films']:
                ACTOR[first_col]['films'][last_col] = ""

    print("\trun parse performances...")
    with gzip.open(output_file_performances, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = return_first_column(decode_line)
            last_col = return_id(decode_line)

            if first_col not in PERF_FILM:
                PERF_FILM[first_col] = last_col

    print("\trun parse other...")
    with gzip.open(output_file_other, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = return_first_column(decode_line)

            if first_col in ACTOR:
                if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line):
                    ACTOR[first_col]['name'] = return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", decode_line):
                    ACTOR[first_col]['alias'] = return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]person[.]date_of_birth>", decode_line):
                    ACTOR[first_col]['b_date'] = return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]deceased_person[.]date_of_death>", decode_line):
                    ACTOR[first_col]['d_date'] = return_name_or_date(decode_line)
            else:
                if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line) \
                        and first_col not in FILM_ID_NAME:
                    FILM_ID_NAME[first_col] = return_name_or_date(decode_line)

    print("\nrun PARRING...")
    print("\trun parring...")
    for actor_key, actor_value in ACTOR.items():
        for film_key in actor_value['films'].keys():
            if film_key in PERF_FILM:
                ACTOR[actor_key]['films'][film_key] = \
                    FILM_ID_NAME[PERF_FILM[film_key]] if PERF_FILM[film_key] in FILM_ID_NAME else "NONE"

    print("\nrun SORT, WRITE AND INDEXING...")
    print("\trun sort...")
    sorted(ACTOR)
    print("\trun write...")
    f = open_file(output_file_final)
    for actor_key, actor_value in ACTOR.items():
        if actor_value['name']:
            line = "<" + actor_value['name'] + ">"
            line += " <" + actor_value['alias'] + ">" if actor_value['alias'] else " <NONE>"
            line += " <" + actor_value['b_date'] + ">" if actor_value['b_date'] else " <0001-01-01>"
            line += " <" + actor_value['d_date'] + ">" if actor_value['d_date'] \
                else " <NOW>"
            for film_value in actor_value['films'].values():
                line += " <" + film_value + ">" if film_value else ""
            f.write(line)
            f.write("\n")
    f.close()

    search()
elif cmd == "n":
    search()
else:
    print("Unknown input")
