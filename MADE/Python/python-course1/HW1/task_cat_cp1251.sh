#!/bin/bash
cat queries_cp1251.txt | ./inverted_index.py query --query-file-cp1251 -

#iconv -f utf-8 -t cp1251
