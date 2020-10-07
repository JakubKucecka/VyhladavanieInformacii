#!/usr/bin/env python3


def pair(ACTOR, PERF_FILM, FILM_ID_NAME):
    print("\nrun PAIRING...")
    print("\trun pairing...")
    for actor_key, actor_value in ACTOR.items():
        for film_key in actor_value['films'].keys():
            if film_key in PERF_FILM:
                ACTOR[actor_key]['films'][film_key] = \
                    FILM_ID_NAME[PERF_FILM[film_key]] if PERF_FILM[film_key] in FILM_ID_NAME else "NONE"
    return ACTOR
