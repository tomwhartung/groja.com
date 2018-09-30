#!/bin/bash
#
# print the contents of our sqlite3 database
#
export PYTHONPATH="..:${PYTHONPATH}"

## python3 -m db_access
python3 -c "from db_access import print_table ; print_table()"
