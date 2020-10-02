#!/usr/bin/env python3
import gzip
import os

# input_file = input("Enter full path your file: ")
input_file = '../etc/film_dump_from_freebase_rdf.gz'
output_file = "../etc/film_dump.gz"


def open_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return gzip.open(file_name, "wt", encoding="utf-8")


lines = []

with gzip.open(input_file, 'rb') as f:
    fa = open_file(output_file)
    count = 0

    for line in f:

        decode_line = line.decode("utf-8")
        count += 1

        fa.write("<http://rdf.freebase.com/ns/" + decode_line[1:-2] + "  .\n")

        if count % 1000000 == 0:
            print("line: " + str(f'{count: }') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")

    print("line: " + str(f'{count: }') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")
    fa.close()

print("DONE")
