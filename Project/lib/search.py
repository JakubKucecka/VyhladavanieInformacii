#!/usr/bin/env python3

from datetime import datetime
import gzip
import lib.handler as handler
import re


def search(final_actor_file, final_film_file):
    not_end = "y"

    while not_end == "y":
        print("\nrun SEARCH...")
        print("\trun search...")
        name_1 = input("\nEnter first name: ")
        name_2 = input("Enter second name: ")

        if name_1.upper() == name_2.upper():
            print("Enter diferent names!")
            continue

        with gzip.open(final_actor_file, 'rb') as f:
            persons = []
            num_of_actors = 0

            for line in f:
                decode_line = line.decode("utf-8")
                array_line = handler.return_array(decode_line)

                if name_1.upper() in array_line[0].upper().split('\t ') \
                        or name_2.upper() in array_line[0].upper().split('\t ') \
                        or name_1.upper() in array_line[1].upper().split('\t ') \
                        or name_2.upper() in array_line[1].upper().split('\t '):
                    con = 0
                    i = -1
                    for actor in persons:
                        i += 1
                        for film_name in actor[0].split(', '):
                            if film_name.upper() in array_line[0].upper().split('\t ') \
                                    or film_name.upper() in array_line[1].upper().split('\t '):
                                con = 1
                                break

                        if not con:
                            for film_name in actor[1].split(', '):
                                if re.search(film_name.upper(), array_line[0].upper()) \
                                        or re.search(film_name.upper(), array_line[1].upper()):
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
                print("The actor " + name_1 + " or " + name_2 + " not found")
            else:
                if datetime.strptime(persons[0][2], '%Y-%m-%d') <= datetime.strptime(persons[1][3], '%Y-%m-%d') \
                        and datetime.strptime(persons[1][2], '%Y-%m-%d') <= datetime.strptime(persons[0][3],
                                                                                              '%Y-%m-%d'):
                    films_array = []
                    if len(persons[0]) > 4 and len(persons[1]) > 4:
                        for film_p1 in persons[0][4:]:
                            for film_p2 in persons[1][4:]:
                                if film_p1.upper() == film_p2.upper():
                                    films_array.append(film_p1)

                    if films_array:
                        if name_1.upper() in persons[0][0].upper().split('\t ') \
                                or name_1.upper() in persons[0][1].upper().split('\t '):
                            alias_1 = ", ".join(persons[0][0].split('\t '))
                            if "NONE" not in persons[0][1].split('\t '):
                                alias_1 += ", " + ", ".join(persons[0][1].split('\t '))
                            alias_2 = ", ".join(persons[1][0].split('\t '))
                            if "NONE" not in persons[1][1].split('\t '):
                                alias_2 += ", " + ", ".join(persons[1][1].split('\t '))
                        else:
                            alias_2 = ", ".join(persons[0][0].split('\t '))
                            if "NONE" not in persons[0][1].split('\t '):
                                alias_2 += ", " + ", ".join(persons[0][1].split('\t '))
                            alias_1 = ", ".join(persons[1][0].split('\t '))
                            if "NONE" not in persons[1][1].split('\t '):
                                alias_1 += ", " + ", ".join(persons[1][1].split('\t '))

                        print("Actors: \n\t" + name_1 + " -> " + alias_1 + "\n\t" + name_2 + " -> "
                              + alias_2 + "\nplayed together in films:")
                        with gzip.open(final_film_file, 'rb') as ff:
                            films_count = len(films_array)
                            for film_line in ff:
                                decode_line = film_line.decode("utf-8")
                                array_film_line = handler.return_array(decode_line)

                                for film in films_array:
                                    if film == array_film_line[0]:
                                        print("\t" + array_film_line[1].split('\t ')[0] + " -> "
                                              + ", ".join(array_film_line[1].split('\t ')))
                                        films_count -= 1

                                if films_count == 0:
                                    break
                    else:
                        print("Actors " + name_1 + " and " + name_2 + " did not play together")
                else:
                    if name_1.upper() in persons[0][0].upper().split('\t ') \
                            or name_1.upper() in persons[0][1].upper().split('\t '):
                        date_1 = "born in: " + persons[0][2] + " and died in: " + persons[0][3]
                        date_2 = "born in: " + persons[1][2] + " and died in: " + persons[1][3]
                    else:
                        date_2 = persons[0][2] + "-" + persons[0][3]
                        date_1 = persons[1][2] + "-" + persons[1][3]
                    print("Actors:\n\t" + name_1 + " -> " + date_1
                          + "\n\t" + name_2 + " -> " + date_2
                          + "\nActors could not play together because they did not live at the same time")

        not_end = input("\nDo you want to continue? [y|n]: ")

    return not_end
