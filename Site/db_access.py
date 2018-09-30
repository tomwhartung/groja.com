""" db_access.py: Routines to support accessing the sqlite3 db

Purpose: create db containing a single table named NameEmail
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference (for Flask DB patterns):
  http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
Usage:
  Print all rows in db
    python3 -m db_access
    bin/print.sh
"""

import datetime
import sqlite3
from db_create import NAME_EMAIL_TABLE

# =============================================================================
#
# Database access functions
# -------------------------


def update_or_insert_name_email(
          name, email, id=0, consulting=-1, newsletter=-1, portrait=-1):

    """ Update an old or insert a new row into the table, as appropriate """

    # print('update_or_insert_name_email NAME_EMAIL_TABLE =', NAME_EMAIL_TABLE)
    if id == 0:
        result = email_already_in_db(email)
        if result:
            id = result[0]
            # print('Updating the email that is already in the db, id =', id)
            with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
                query = 'UPDATE NameEmail SET name = "' + name + '"'
                if consulting != -1:
                    query += ', consulting = ' + str(consulting)
                if newsletter != -1:
                    query += ', newsletter = ' + str(newsletter)
                if portrait != -1:
                    query += ', portrait = ' + str(portrait)
                query += ' WHERE id = ' + str(id)
                curs = connection.cursor()
                curs.execute(query)
        else:
            # default ("-1") means not specified means "0" when inserting
            if consulting == -1:
                consulting = 0
            if newsletter == -1:
                newsletter = 0
            if portrait == -1:
                portrait = 0
            insert_name_email(name, email, consulting, newsletter, portrait)
    else:
        print('Current code unable to process passed-in id:', id)

    return True


def email_already_in_db(email):

    """ If email address is in db, return the row, else return False """

    result = False
    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        # query = 'SELECT * from NameEmail WHERE email = "' + email + "'"
        query = 'SELECT * from NameEmail WHERE email = "' + email + '"'
        curs.execute(query)
        row = curs.fetchone()
        # print('in email_already_in_db, row:', row)
        result = row
    return result


def insert_name_email(name, email, consulting=0, newsletter=0, portrait=0):

    """ Insert a row into the table """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute(
            "INSERT INTO NameEmail " +
            "(name,email,consulting,newsletter,portrait) " +
            "VALUES (?,?,?,?,?)",
            (name, email, consulting, newsletter, portrait)
        )
    return True


def my_current_timestamp():

    """ Return the date and time formatted as '1970-01-01 00:00:00' """
    """ This matches the format of the Sqlite3 CURRENT_TIMESTAMP """

    my_time = datetime.time(1, 2, 3)
    my_date = datetime.date.today()
    my_current_timestamp = datetime.datetime.combine(my_date, my_time)
    return my_current_timestamp


def print_table(line_prefix=""):

    """ Print all rows in the table to stdout """

    rows = get_data()
    see_data(rows, line_prefix)
    return True


# =============================================================================
#
# Functions for testing and development, etc.:
# --------------------------------------------
# All of this code is cruft and should be ignored and even deleted!
#


def insert_hard_coded_name_email():

    """ Insert a row of hard-coded values into the table """

    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        my_ts = my_current_timestamp()
        curs.execute(
            "INSERT INTO NameEmail " +
            "(name,email,date_added,date_changed) " +
            "VALUES (?,?,?,?)",
            ('Sam', 'sam@sam.com', my_ts, my_ts)
        )
    return True


def get_data():

    """ Get the data """

    rows = []
    with sqlite3.connect(NAME_EMAIL_TABLE) as connection:
        curs = connection.cursor()
        curs.execute('SELECT * from NameEmail')
        rows = curs.fetchall()
    return rows


def see_data(rows, line_prefix=""):

    """ Print the data """

    for row in rows:
        print(line_prefix, "row:", row)
    return True


def test_insert_functions():

    """ Test our insert* Functions
    Usage:
        $ . ./env.sh
        $ python3
        >>> from db_access import test_insert_functions
        >>> test_insert_functions()
    Or, use these commands to test on the command line:
        $ . ./env.sh
        $ python3
        >>> from db_access import insert_hard_coded_name_email
        >>> insert_hard_coded_name_email()
        >>> from db_access import insert_name_email
        >>> insert_name_email('june', 'june@may.com')
        >>> insert_name_email('april', 'april@may.com', portrait=1)
        >>> insert_name_email('pete', 'pete@example.com', consulting=1)
        >>> insert_name_email('mia', 'mia@example.com', newsletter=1)
    """
    print_table("1:")
    insert_hard_coded_name_email()
    print('')
    print_table("2:")
    insert_name_email('june', 'june@may.com')
    print('')
    print_table("3:")
    insert_name_email('april', 'april@may.com', portrait=1)
    print('')
    print_table("4:")
    insert_name_email('pete', 'pete@example.com', consulting=1)
    print('')
    print_table("5:")
    insert_name_email('mia', 'mia@example.com', newsletter=1)
    print('')
    print_table("6:")

# =============================================================================
#
# When run as a module, print the table
#
if __name__ == '__main__':
    print_table()
