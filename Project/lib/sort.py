#!/usr/bin/env python3

import lib.handler as handler


def sort(ACTOR, final_file):
    print("\nrun SORT, WRITE AND INDEXING...")
    print("\trun sort...")
    ACTOR = {k: v for k, v in sorted(ACTOR.items(), key=lambda item: item[1]['name'])}
    # sorted(ACTOR)
    print("\trun write...")
    f = handler.open_file(final_file)
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
