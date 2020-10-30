#!/usr/bin/env python3

import gzip
import lib.handler as handler
import re


def pars(actors_file, performances_file, other_file, ACTOR, PERF_FILM, FILM_ID_NAME):
    print("\nrun PARSE...")

    print("\trun parse actors...")
    with gzip.open(actors_file, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = handler.return_first_column(decode_line)
            last_col = handler.return_id(decode_line)
            if first_col not in ACTOR:
                ACTOR[first_col] = {'name': [], 'alias': [], 'b_date': "", 'd_date': "", 'films': {last_col: "NONE"}}
            if first_col in ACTOR and last_col not in ACTOR[first_col]['films']:
                ACTOR[first_col]['films'][last_col] = "NONE"

    print("\trun parse performances...")
    with gzip.open(performances_file, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = handler.return_first_column(decode_line)
            last_col = handler.return_id(decode_line)

            if first_col not in PERF_FILM:
                PERF_FILM[first_col] = last_col

    print("\trun parse other...")
    with gzip.open(other_file, 'rb') as f:
        for line in f:
            decode_line = line.decode("utf-8")
            first_col = handler.return_first_column(decode_line)

            if first_col in ACTOR:
                if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line):
                    name = handler.return_name_or_date(decode_line)
                    if name not in ACTOR[first_col]['name']:
                        while 1:
                            if name[0] == " ":
                                name = name[1:]
                            else:
                                break
                        ACTOR[first_col]['name'].append(name)
                elif re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", decode_line):
                    alias = handler.return_name_or_date(decode_line)
                    if alias not in ACTOR[first_col]['alias']:
                        while 1:
                            if alias[0] == " ":
                                alias = alias[1:]
                            else:
                                break
                        ACTOR[first_col]['alias'].append(alias)
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]person[.]date_of_birth>", decode_line):
                    date = handler.return_name_or_date(decode_line)
                    if len(date) == 4:
                        date += "-01-01"
                    if len(date) == 10:
                        ACTOR[first_col]['b_date'] = date
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]deceased_person[.]date_of_death>",
                               decode_line):
                    date = handler.return_name_or_date(decode_line)
                    if len(date) == 4:
                        date += "-01-01"
                    if len(date) == 10:
                        ACTOR[first_col]['d_date'] = date
            else:
                if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line) \
                        or re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", decode_line):
                    film = handler.return_name_or_date(decode_line)
                    if first_col not in FILM_ID_NAME:
                        FILM_ID_NAME[first_col] = []
                    if re.match(r'[a-zA-Z0-9,. ]+', film) and film not in FILM_ID_NAME[first_col]:
                        FILM_ID_NAME[first_col].append(film)

    return [ACTOR, PERF_FILM, FILM_ID_NAME]
