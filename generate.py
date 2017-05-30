#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import time
import random
import string

import sqlite3

TYPE_A = 'letter_only'
TYPE_B = 'digit_only'
TYPE_C = 'letter_digit'
TYPE_D = 'printtable'


def get_db_name():
    db_name = "passwd.db"
    if os.path.exists(db_name):
        return db_name

    sql = """ create table passwd(
                                    id integer primary key not null,
                                    passwd varchar(20) not null,
                                    created_at varchar(20) not null
                                );
          """

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return db_name

def insert_into_db(passwd, created_at):
    db_name = get_db_name()
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("insert into passwd(passwd, created_at) values(?, ?)", (passwd, created_at))
    conn.commit()
    conn.close()

def generate_passwd(type_, lens=12):
    if type_ == TYPE_A:
        base = string.ascii_letters
    elif type_ == TYPE_B:
        base = string.digits
    elif type_ == TYPE_C:
        base = string.ascii_letters + string.digits
    else:
        base = string.printable[0:-32]

    passwd = ''.join(random.sample(base, lens))

    return passwd

def run():
    passwd = generate_passwd(TYPE_D, 12)
    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    insert_into_db(passwd, created_at)
    print created_at, passwd

if __name__ == "__main__":
    run()

