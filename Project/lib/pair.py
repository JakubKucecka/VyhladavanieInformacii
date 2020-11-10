#!/usr/bin/env python3


"""
the function pairs the dictionary

input:
     dictionary ACTOR, PERF_FILM, FILM_ID_NAME

output:
     final form dictionary ACTOR
"""


def pair(ACTOR, PERF_FILM, FILM_ID_NAME):
    print("\nrun PAIRING...")
    print("\trun pairing...")
    for actor_key, actor_value in ACTOR.items():
        for film_key in actor_value['films'].keys():
            if film_key in PERF_FILM and PERF_FILM[film_key] in FILM_ID_NAME:
                films = FILM_ID_NAME[PERF_FILM[film_key]]
                if PERF_FILM[film_key] != films[0]:
                    films.insert(0, PERF_FILM[film_key])
                ACTOR[actor_key]['films'][film_key] = films
    return ACTOR
