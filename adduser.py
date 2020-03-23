""" Add a new user to the quiz.db for each user in the users.csv file. """

import sqlite3
import hashlib


def add_user(user, pwd, tipe):
    """ Add a new user to the quiz.db, commit the changes and close the connection. """

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    text = 'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'
    cursor.execute(text.format(user, pwd, tipe))
    conn.commit()
    conn.close()


with open('users.csv', 'r') as file:
    LINES = file.read().splitlines()

for users in LINES:
    (_user, _pwd, _tipe) = users.split(',')
    print(_user)
    print(_tipe)
    add_user(_user, hashlib.md5(_pwd.encode()).hexdigest(), _tipe)
