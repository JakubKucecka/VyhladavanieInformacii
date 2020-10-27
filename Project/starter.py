#!/usr/bin/env python3

import lib.pars as pars
import lib.dump as dump
import lib.pair as pair
import lib.sort as sort
import lib.search as search

input_file = 'D:/STU/VI/Project/tmp/parse/film_dump_from_freebase_rdf.gz'
# input_file = 'D:/STU/VI/Project/tmp/parse/tmp_film.gz'
actors_file = "D:/STU/VI/Project/tmp/parse/actors.gz"
performances_file = "D:/STU/VI/Project/tmp/parse/performances.gz"
other_file = "D:/STU/VI/Project/tmp/parse/other.gz"
final_actor_file = "D:/STU/VI/Project/tmp/parse/final_actor.gz"
final_film_file = "D:/STU/VI/Project/tmp/parse/final_film.gz"

ACTOR = {}
PERF_FILM = {}
FILM_ID_NAME = {}

cmd = input("\nDo you want to run a dump? [y|n]: ")
if cmd == "y":
    # input_file = input("Enter full path your file: ")
    dump.dump(input_file, actors_file, performances_file, other_file)
elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

cmd = input("\nDo you want to run a pars, pair and sort? [y|n]: ")
if cmd == "y":
    [ACTOR, PERF_FILM, FILM_ID_NAME] = pars.pars(actors_file, performances_file, other_file, ACTOR, PERF_FILM, FILM_ID_NAME)

    ACTOR = pair.pair(ACTOR, PERF_FILM)

    sort.sort(ACTOR, FILM_ID_NAME, final_actor_file, final_film_file)
elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

cmd = input("\nDo you want to run a search? [y|n]: ")
if cmd == "y":
    ret = search.search(final_actor_file, final_film_file)
    if ret != "n":
        print("ERROR: Unknown input")
        exit(1)
elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

print("\nDone")
exit(0)
