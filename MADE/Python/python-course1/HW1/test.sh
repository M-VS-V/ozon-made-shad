#!/bin/bash
pytest -vv test_Mashinson_Vsevolod_inverted_index.py --cov=task_Mashinson_Vsevolod_inverted_index --cov-branch $1
coverage report -m