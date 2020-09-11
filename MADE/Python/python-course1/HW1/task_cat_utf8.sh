#!/bin/bash
cat queries_utf8.txt | ./inverted_index.py build --index query --query-file-utf8 -