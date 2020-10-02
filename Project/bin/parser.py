#!/usr/bin/env python3
import gzip
import os
import re
import locale

locale.setlocale(locale.LC_ALL, '')

# input_file = input("Enter full path your file: ")
input_file = '../etc/film_dump_from_freebase_rdf.gz'
output_file_actors = "../etc/parse/actors.gz"
output_file_performances = "../etc/parse/performances.gz"
output_file_films = "../etc/parse/films.gz"


def return_first_column(input_line):
    return input_line[input_line.find("<"): input_line.find(">") + 1]


def open_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return gzip.open(file_name, "wt", encoding="utf-8", newline='')


lines = []

with gzip.open(input_file, 'rb') as f:
    fa = open_file(output_file_actors)
    fp = open_file(output_file_performances)
    ff = open_file(output_file_films)
    actual_ids = ""
    count = 0

    for line in f:

        decode_line = line.decode("utf-8")
        count += 1

        if return_first_column(decode_line) != actual_ids:
            control_film = ""

            for l in lines:
                if re.search(
                        "^<http://rdf.freebase.com/ns/[m|g][.].*>[ ]*<http://rdf[.]freebase[.]com/ns/film[.]actor.*>[ ]*<.*>.*$",
                        l):
                    control_film = "a"
                    break
                elif re.search(
                        "^<http://rdf.freebase.com/ns/[m|g][.].*>[ ]*<http://rdf[.]freebase[.]com/ns/film[.]performance.*>[ ]*<.*>.*$",
                        l):
                    control_film = "p"
                    break
                elif re.search(
                        "^<http://rdf.freebase.com/ns/[m|g][.].*>[ ]*<http://rdf[.]freebase[.]com/ns/film[.]film.*>[ ]*<.*>.*$",
                        l):
                    control_film = "f"
                    break
                else:
                    continue

            if control_film == "a":
                for l in lines:
                    if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", l) \
                            or re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", l) \
                            or re.search("<http://rdf[.]freebase[.]com/ns/people[.]person[.]date_of_birth>", l) \
                            or re.search("<http://rdf[.]freebase[.]com/ns/people[.]deceased_person[.]date_of_death>", l) \
                            or re.search("<<http://rdf[.]freebase[.]com/ns/film[.]actor[.]film>>", l):
                        fa.write(l)
                print("line: " + str(f'{count:n}') + ", " + str(f'{(count * 100 / 114328618):03.2f}')
                      + "%, ids: " + actual_ids + ", write actor")
            elif control_film == "p":
                for l in lines:
                    if re.search("<http://rdf[.]freebase[.]com/ns/film[.]performance[.]film>", l):
                        fp.write(l)
                print("line: " + str(f'{count:n}') + ", " + str(f'{(count * 100 / 114328618):03.2f}')
                      + "%, ids: " + actual_ids + ", write performance")
            elif control_film == "f":
                for l in lines:
                    if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", l) \
                            or re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", l):
                        ff.write(l)
                print("line: " + str(f'{count:n}') + ", " + str(f'{(count * 100 / 114328618):03.2f}')
                      + "%, ids: " + actual_ids + ", write film, ")

            lines = []
            actual_ids = return_first_column(decode_line)
            lines.append(decode_line)

        else:
            lines.append(decode_line)

        if count % 1000000 == 0:
            print("line: " + str(f'{count:n}') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")

    print("line: " + str(f'{count: }') + ", " + str(f'{(count * 100 / 114328618):03.2f}') + "%")
    fa.close()
    fp.close()
    ff.close()

print("DONE")
