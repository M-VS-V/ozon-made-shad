#!/bin/bash
cat queries.txt | ./inverted_index.py query --query-file-utf8 -
