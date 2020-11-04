#!/usr/bin/env python3

import gzip
import lib.handler as handler
import re


"""
podla regexov deli riadky do prislusnych suborov

vstup:
    cesta k prislusnym suborom
    
vystup:
    zapisane subory
"""
def dump(input_file, actors_file, performances_file, other_file):
    cmd = input("\nAre you sure you want to overwrite the other.gz, performance.gz and actor.gz files? [y|n]: ")
    if cmd == "y":
        print("run DUMP...")
        lines = []

        with gzip.open(input_file, 'rb') as f:
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

            # for line in f:
            #
            #     decode_line = line.decode("utf-8")
            #     count += 1
            #
            #     if re.search(
            #             r"^<http://rdf.freebase.com/ns/.*>[ ]*<http://rdf\.freebase\.com/ns/film\.actor\.film.*>[ ]*<.*>.*$",
            #             decode_line):
            #         fa.write(decode_line)
            #     elif re.search(
            #             r"^<http://rdf.freebase.com/ns/.*>[ ]*<http://rdf\.freebase\.com/ns/film\.performance\.film.*>[ ]*<.*>.*$",
            #             decode_line):
            #         fp.write(decode_line)
            #     elif re.search(
            #             r'<http://rdf\.freebase\.com/ns/type\.object\.name>[ ]*"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+".*',
            #             decode_line) \
            #             or re.search(
            #         r'<http://rdf\.freebase\.com/ns/common\.topic\.alias>.*\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
            #         decode_line) \
            #             or re.search(
            #         r'http://rdf\.freebase\.com/ns/people\.person\.date_of_birth>[ ]*\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
            #         decode_line) \
            #             or re.search(
            #         r'http://rdf\.freebase\.com/ns/people\.deceased_person\.date_of_death>[ ]*\"[a-zA-Z0-9á-žÁ-ŽА-Яа-я,.\"\\\-:\'_ ]+\".*',
            #         decode_line):
            #         fo.write(decode_line)

                if count % 1000000 == 0:
                    print("line: " + str(f'{count / 1000000: }') + "M, " + str(
                        f'{(count * 100 / 3140000000):03.2f}') + "%")

            fa.close()
            fp.close()
            fo.close()

    elif cmd != "n":
        print("ERROR: Unknown input")
        exit(1)
