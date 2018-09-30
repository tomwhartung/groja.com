""" Create a sqlite3 db for the NameEmail table

Purpose: Create the db, create the table, seed in one row of data
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference (for Flask DB patterns):
  http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
Usage:
  Create the db and seed it with one row of data
    python3 -m db_create
    db_create.sh
"""

import sqlite3
from flask import Flask   # Note: this file has no routes (see comments below)

DB_DIRECTORY = '/var/www/groja.com/htdocs/groja.com/db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

app = Flask(__name__)   # Declaring app so we can call open_resource

# =============================================================================
#
# Functions
# ---------


def drop_table():

    """ Drop the table exists (if it exists) """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute('DROP TABLE IF EXISTS NameEmail')
    return True


def create_table():

    """ Read schema and create the database (if necessary) and table """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        schema = DB_DIRECTORY + 'NameEmailSchema.sql'
        with app.open_resource(schema, mode='r') as nameEmailSchema:
            connection.executescript(nameEmailSchema.read())
            connection.commit()
    return True


def seed_table():

    """ Insert a row in the table, as a sanity check """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute(
            "INSERT INTO NameEmail (name,email) VALUES (?,?)",
            ('Joe', 'joe@joe.com')
        )
    return True

# =============================================================================
#
# When run as a module, drop, create, and seed the table
#
if __name__ == '__main__':
    drop_table()
    create_table()
    seed_table()
