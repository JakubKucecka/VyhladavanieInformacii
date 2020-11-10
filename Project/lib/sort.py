#!/usr/bin/env python3

import lib.handler as handler

"""
the function organizes the ACTOR dictionary, writes it in the appropriate form to the file

input:
    dictionary ACTOR and the path to the final file
    
output:
    the file is written
"""


def sort(ACTOR, final_file):
    print("\nrun SORT, WRITE AND INDEXING...")
    print("\trun sort...")
    ACTOR = {k: v for k, v in sorted(ACTOR.items(), key=lambda item: item[1]['name'])}
    print("\trun write...")
    f = handler.open_file(final_file)
    for actor_key, actor_value in ACTOR.items():
        if actor_value['name']:
            names = '\t'.join(actor_value['name'])
            line = "<" + names + ">"
            aliases = '\t'.join(actor_value['alias'])
            line += " <" + aliases + ">" if aliases else " <NONE>"
            line += " <" + actor_value['b_date'] + ">" if actor_value['b_date'] else " <0001-01-01>"
            line += " <" + actor_value['d_date'] + ">" if actor_value['d_date'] else " <NOW>"
            writed_films = []
            for film_value in actor_value['films'].values():
                if film_value != "NONE" and film_value[0] not in writed_films:
                    line += " <" + "\t".join(film_value) + ">"
                    writed_films.append(film_value[0])
            f.write(line)
            f.write("\n")
    f.close()
