#!/usr/bin/env python3

import gzip
import lib.handler as handler
import re


def dump(input_file, actors_file, performances_file, other_file):
    print("run DUMP...")
    with gzip.open(input_file, 'rb') as f:
        fa = handler.open_file(actors_file)
        fp = handler.open_file(performances_file)
        fo = handler.open_file(other_file)
        count = 0

        for line in f:

            decode_line = line.decode("utf-8")
            count += 1

            if re.search(
                    "^<http://rdf.freebase.com/ns/.*>[ ]*<http://rdf\.freebase\.com/ns/film\.actor\.film.*>[ ]*<.*>.*$",
                    decode_line):
                fa.write(decode_line)
            elif re.search(
                    "^<http://rdf.freebase.com/ns/.*>[ ]*<http://rdf\.freebase\.com/ns/film\.performance\.film.*>[ ]*<.*>.*$",
                    decode_line):
                fp.write(decode_line)
            elif re.search("<http://rdf\.freebase\.com/ns/type\.object\.name>", decode_line) \
                    or re.search("<http://rdf\.freebase\.com/ns/common\.topic\.alias>", decode_line) \
                    or re.search("<http://rdf\.freebase\.com/ns/people\.person\.date_of_birth>", decode_line) \
                    or re.search("<http://rdf\.freebase\.com/ns/people\.deceased_person\.date_of_death>", decode_line):
                fo.write(decode_line)

            if count % 1000000 == 0:
                print("Read: " + str(count / 1000000) + "M lines from file: " + input_file)

        fa.close()
        fp.close()
        fo.close()
