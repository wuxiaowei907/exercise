# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv

with open(file_name) as fin:
    print fin.read()

    
