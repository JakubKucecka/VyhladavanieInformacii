#!/usr/bin/env python3

from datetime import datetime
import gzip
import lib.handler as handler


def search(final_file):
    not_end = "y"

    while not_end == "y":
        print("\nrun SEARCH...")
        print("\trun search...")
        name_1 = input("\nEnter first name: ")
        name_2 = input("Enter second name: ")

        if name_1.upper() == name_2.upper():
            print("ERROR: Enter diferent names")
            continue

        with gzip.open(final_file, 'rb') as f:
            persons = []
            num_of_actors = 0

            for line in f:
                decode_line = line.decode("utf-8")
                array_line = handler.return_array(decode_line)

                if array_line[0].upper() == name_1.upper() or array_line[0].upper() == name_2.upper():
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
                print("ERROR: The actor " + name_1 + " or " + name_2 + " not found")
            else:
                if datetime.strptime(persons[0][2], '%Y-%m-%d') <= datetime.strptime(persons[1][3], '%Y-%m-%d') \
                        and datetime.strptime(persons[1][2], '%Y-%m-%d') <= datetime.strptime(persons[0][3],
                                                                                              '%Y-%m-%d'):

                    films = ""
                    if len(persons[0]) > 4 and len(persons[1]) > 4:
                        films_array = []
                        for film_p1 in persons[0][4:]:
                            for film_p2 in persons[1][4:]:
                                if film_p1.upper() == film_p2.upper():
                                    films_array.append(film_p1)

                        films = ','.join(films_array)
                    if films:
                        print("Actors " + name_1 + " and " + name_2 + " played together in films: " + films)
                    else:
                        print("ERROR: The actors " + name_1 + " and " + name_2 + " did not play together")
                else:
                    print("ERROR: The actors " + name_1 + " and " + name_2
                          + "  could not play together because they did not live at the same time")

        not_end = input("\nDo you want to continue? [y|n]: ")

    return not_end
