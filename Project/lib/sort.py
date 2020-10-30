#!/usr/bin/env python3

import lib.handler as handler


def sort(ACTOR, FILM_ID_NAME, final_actor_file, final_film_file):
    print("\nrun SORT, WRITE AND INDEXING...")
    print("\trun sort...")
    ACTOR = {k: v for k, v in sorted(ACTOR.items(), key=lambda item: item[1]['name'])}
    sorted(FILM_ID_NAME)
    print("\trun write...")
    f = handler.open_file(final_actor_file)
    for actor_key, actor_value in ACTOR.items():
        if actor_value['name']:
            names = '\t'.join(actor_value['name'])
            line = "<" + names + ">"
            aliases = '\t'.join(actor_value['alias'])
            line += " <" + aliases + ">" if aliases else " <NONE>"
            line += " <" + actor_value['b_date'] + ">" if actor_value['b_date'] else " <0001-01-01>"
            line += " <" + actor_value['d_date'] + ">" if actor_value['d_date'] else " <NOW>"
            for film_value in actor_value['films'].values():
                if film_value != "NONE":
                    line += " <" + film_value + ">"
            f.write(line)
            f.write("\n")
    f.close()

    f = handler.open_file(final_film_file)
    for film_key, film_value in FILM_ID_NAME.items():
        line = "<" + film_key + ">"
        films = '\t'.join(film_value)
        line += " <" + films + ">" if films else " <NONE>"
        f.write(line)
        f.write("\n")
    f.close()
