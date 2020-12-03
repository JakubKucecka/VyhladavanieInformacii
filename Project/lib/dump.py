#!/usr/bin/env python3

import pathlib
import gzip
import lib.handler as handler
import re

"""
according to regex, it divides the rows into appropriate files

input:
    path to the relevant files, and test feature
    
output:
    registered files
"""


def dump(actors_file, performances_file, other_file, test):
    if not test:
        cmd = input("\nAre you sure you want to overwrite the other.gz, performance.gz and actor.gz files? [y|n]: ")
    else:
        cmd = "y"
    if cmd == "y":
        file_name = input("\nEnter full path to the file: ")

        file = pathlib.Path(file_name)
        if not file.exists():
            print("ERROR: \n\tFile: " + file_name + " not exist!")
            exit(1)

        print("run DUMP...")
        lines = []

        with gzip.open(file_name, 'rb') as f:
            fa = handler.open_file(actors_file)
            fp = handler.open_file(performances_file)
            fo = handler.open_file(other_file)

            count = 0
            actual_id = ""
            for line in f:
                decode_line = line.decode("utf-8")
                resolve_id = handler.return_first_column(decode_line)
                count += 1
                if resolve_id != actual_id:
                    control_film = 0
                    for l in lines:
                        if l.find("film.") > 0:
                            control_film = 1
                            break
                        else:
                            continue
                    if control_film > 0:
                        for l in lines:
                            if re.search(
                                    r"<.*>.+<http://rdf\.freebase\.com/ns/film\.actor\.film>.+<.*>", l):
                                fa.write(l)
                            elif re.search(
                                    r"<.*>.+<http://rdf\.freebase\.com/ns/film\.performance\.film>.+<.*>", l):
                                fp.write(l)
                            elif re.search(
                                    r'<http://rdf\.freebase\.com/ns/type\.object\.name>.+"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+".*',
                                    l) \
                                    or re.search(
                                r'<http://rdf\.freebase\.com/ns/common\.topic\.alias>.+\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
                                l) \
                                    or re.search(
                                r'http://rdf\.freebase\.com/ns/people\.person\.date_of_birth>.+\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
                                l) \
                                    or re.search(
                                r'http://rdf\.freebase\.com/ns/people\.deceased_person\.date_of_death>.+\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
                                l):
                                fo.write(l)

                    lines = []
                    actual_id = resolve_id
                    lines.append(decode_line)
                else:
                    lines.append(decode_line)

                if count % 1000000 == 0:
                    print("line: " + str(f'{count / 1000000: }') + "M")

            fa.close()
            fp.close()
            fo.close()

    elif cmd != "n":
        print("ERROR: Unknown input")
        exit(1)
