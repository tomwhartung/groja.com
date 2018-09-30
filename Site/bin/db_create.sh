#!/bin/bash
#
# Create and print the db
#
export PATH=".:${PATH}"
export PYTHONPATH="..:${PYTHONPATH}"

python3 -m db_create
print.sh
