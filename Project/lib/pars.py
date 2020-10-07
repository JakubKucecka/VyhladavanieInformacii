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
                ACTOR[first_col] = {'name': "", 'alias': "", 'b_date': "", 'd_date': "", 'films': {last_col: ""}}
            if first_col in ACTOR and last_col not in ACTOR[first_col]['films']:
                ACTOR[first_col]['films'][last_col] = ""

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
                    ACTOR[first_col]['name'] = handler.return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/common[.]topic[.]alias>", decode_line):
                    ACTOR[first_col]['alias'] = handler.return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]person[.]date_of_birth>", decode_line):
                    ACTOR[first_col]['b_date'] = handler.return_name_or_date(decode_line)
                elif re.search("<http://rdf[.]freebase[.]com/ns/people[.]deceased_person[.]date_of_death>",
                               decode_line):
                    ACTOR[first_col]['d_date'] = handler.return_name_or_date(decode_line)
            else:
                if re.search("<http://rdf[.]freebase[.]com/ns/type[.]object[.]name>", decode_line) \
                        and first_col not in FILM_ID_NAME:
                    FILM_ID_NAME[first_col] = handler.return_name_or_date(decode_line)
    return [ACTOR, PERF_FILM, FILM_ID_NAME]
