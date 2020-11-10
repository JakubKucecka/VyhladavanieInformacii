#!/usr/bin/env python3

import gzip
import locale
import os
import re

locale.setlocale(locale.LC_ALL, '')

"""
in file are function from cut string to one or more arrays and open .gz files
"""


def return_first_column(input_line):
    tmp_line = re.split('[<>]', input_line)[1]
    return re.split('http://rdf.freebase.com/ns/', tmp_line)[1]


def return_id(input_line):
    tmp_line = re.split('[<>]', input_line)[5]
    return re.split('http://rdf.freebase.com/ns/', tmp_line)[1]


def return_name_or_date(input_line):
    tmp_line = re.split('[<>]', input_line)[4]
    name_or_date = re.split('"', tmp_line)[1]
    if name_or_date:
        return name_or_date
    else:
        return "NONE"


def return_array(input_line):
    tmp_array = re.split('[<>]', input_line)
    ret_array = []
    i = 0
    for item in tmp_array:
        if i % 2 == 1:
            ret_array.append(item)
        i += 1
    return ret_array


def open_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return gzip.open(file_name, "wt", encoding="utf-8", newline='')
