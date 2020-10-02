#!/usr/bin/env python3
import gzip
import os
import locale

locale.setlocale(locale.LC_ALL, '')

input_file = '../../VI_data/freebase-rdf-latest.gz'
output_file = "../etc/film_rdf.gz"


def return_first_column(input_line):
    return input_line[input_line.find("<"): input_line.find(">") + 1]


lines = []

with gzip.open(input_file, 'rb') as f:
    if os.path.exists(output_file):
        os.remove(output_file)
    file = gzip.open(output_file, "wt", encoding="utf-8", newline='')
    count = 0
    actual_id = ""
    for line in f:
        decode_line = line.decode("utf-8")
        resolve_id = return_first_column(decode_line)
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
                print("line: " + str(f'{count: }') + ", ids: " + actual_id + ", write to zip film_rdf")
                for l in lines:
                    file.write(l)
            lines = []
            actual_id = resolve_id
            lines.append(decode_line)
        else:
            lines.append(decode_line)
        if count % 1000000 == 0:
            print("line: " + str(f'{count: }') + ", " + str(f'{(count * 100 / 3140000000):03.2f}') + "%")

    file.close()
print("DONE")
