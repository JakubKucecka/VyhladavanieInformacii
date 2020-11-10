#!/usr/bin/env python3

import lib.pars as pars
import lib.dump as dump
import lib.pair as pair
import lib.sort as sort
import lib.index as index
import lib.search as search

"""
global variables that determine the paths to files
"""
input_file = 'tmp/freebase-rdf-latest.gz'
actors_file = "etc/parse/actors.gz"
performances_file = "etc/parse/performances.gz"
other_file = "etc/parse/other.gz"
final_file = "etc/parse/final.gz"
index_dir = "etc/index"

"""
initialization dictionary
"""
ACTOR = {}
PERF_FILM = {}
FILM_ID_NAME = {}

"""
run the dump function
"""
cmd = input("\nDo you want to run a dump? [y|n]: ")
if cmd == "y":
    dump.dump(input_file, actors_file, performances_file, other_file)

elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

"""
run the pars, pair, and sort / write / index functions
"""
cmd = input("\nDo you want to run a pars, pair and sort? [y|n]: ")
if cmd == "y":
    [ACTOR, PERF_FILM, FILM_ID_NAME] = pars.pars(actors_file, performances_file, other_file, ACTOR, PERF_FILM,
                                                 FILM_ID_NAME)
    ACTOR = pair.pair(ACTOR, PERF_FILM, FILM_ID_NAME)
    del FILM_ID_NAME
    del PERF_FILM
    sort.sort(ACTOR, final_file)
    del ACTOR
    index.index(index_dir, final_file)

elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

"""
launch the search function
"""
cmd = input("\nDo you want to run a search? [y|n]: ")
if cmd == "y":
    ret = search.search(index_dir)
    if ret != "n":
        print("ERROR: Unknown input")
        exit(1)
elif cmd != "n":
    print("ERROR: Unknown input")
    exit(1)

exit(0)
