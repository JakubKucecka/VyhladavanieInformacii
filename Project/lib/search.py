#!/usr/bin/env python3

from datetime import datetime
import lib.index as index

"""
search by movie title or actor

input:
    path to index
    
output:
    a list of actors starring in the movie you're looking for
    a list of films starring two actors
    reason why some actors can't play together
"""


def search(index_dir):
    not_end = "y"

    while not_end == "y":
        print("\nrun SEARCH...")
        print("\trun search...")

        cmd = input("\nYou want to search by actors or movie? [a|m]: ")
        if cmd == "m":
            name = input("\nEnter name of movie: ")

            actors = index.search_film(index_dir, name)

            if not actors or actors == -1:
                print("I didn't find the movie")
                not_end = input("\nDo you want to continue? [y|n]: ")
                continue
            if actors != -2:
                print("\nIn film " + name + " played:")
                for a in actors:
                    print("\t" + a)
            else:
                break

        elif cmd == "a":
            actors = []
            i = 0
            pref_names = []
            pref_name = ""
            while i < 2:
                if i == 0:
                    prefix = 'first'
                else:
                    prefix = 'second'
                name = input("\nEnter " + prefix + " name: ")

                if actors and name.upper() in pref_names:
                    print("\nWARN: actor " + pref_name + " and actor " + name + " can be the same person!")

                actors.append(index.search_actor(index_dir, name))
                if actors[i] == -1 or actors[i] == -2:
                    break

                pref_names = actors[i]['names'].upper().split('\t')
                pref_name = name
                i += 1

            if i != 2:
                if actors[i] == -2:
                    not_end = input("\nDo you want to continue? [y|n]: ")
                continue

            name_1 = ""
            name_2 = ""
            actor_1 = []
            actor_2 = []
            films = []
            for a in actors:
                a['data'][1] = datetime.now().strftime("%Y-%m-%d") if a['data'][1] == "NOW" else a['data'][1]
                if i == 2:
                    actor_1 = a
                    name_1 = a['query']
                else:
                    actor_2 = a
                    name_2 = a['query']
                i -= 1

            if datetime.strptime(actor_1['data'][0], '%Y-%m-%d') <= datetime.strptime(actor_2['data'][1], '%Y-%m-%d') \
                    and datetime.strptime(actor_2['data'][0], '%Y-%m-%d') <= datetime.strptime(actor_1['data'][1],
                                                                                               '%Y-%m-%d'):

                for film_1 in actor_1['films'].split('@'):
                    for film_2 in actor_2['films'].split('@'):
                        if film_1.split('\t')[0] == film_2.split('\t')[0]:
                            films.append(film_1[1:])
                            break

                if films:
                    print("\nActors: \n\t" + name_1 + " -> " + ", ".join(actor_1['names'].split('\t'))
                          + "\n\t" + name_2 + " -> " + ", ".join(actor_2['names'].split('\t'))
                          + "\nplayed together in films:")
                    for f in films:
                        string_1 = ""
                        string_2 = ""
                        if len(f) > 1:
                            string_1 = f.split('\t')[1]
                        if len(f) > 2:
                            string_2 = ", ".join(f.split('\t')[2:])
                        print("\t" + string_1 + " -> " + string_2)
                else:
                    actor_1_films = []
                    actor_2_films = []

                    for f in actor_1['films'].split('@'):
                        if len(f.split('\t')) > 2:
                            actor_1_films.append(f.split('\t')[1])
                    for f in actor_2['films'].split('@'):
                        if len(f.split('\t')) > 2:
                            actor_2_films.append(f.split('\t')[1])

                    print("\nActors played in:\n\t" + name_1 + " -> " + ', '.join(actor_1_films)
                          + "\n\t" + name_2 + " -> " + ', '.join(actor_2_films) + "\nActors did not play together")

            else:
                date_1 = "born: " + actor_1['data'][0] + " died: " + actor_1['data'][1]
                date_2 = "born: " + actor_2['data'][0] + " died: " + actor_2['data'][1]
                print("\nActors:\n\t" + name_1 + " -> " + date_1
                      + "\n\t" + name_2 + " -> " + date_2
                      + "\nActors could not play together because they did not live at the same time")

        else:
            print("ERROR: Unknown input")

        not_end = input("\nDo you want to continue? [y|n]: ")

    return not_end
