import sqlite3
import os


class Connect:
    def __init__(self):
        self.password = None
        self.value = None
        self.names = None
        self.p = None
        self.a = None
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()

    def connect(self):
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS base(name TEXT, password INTEGER) ')
        self.con.commit()

    def log(self):
        self.cur.execute('SELECT * FROM base')
        self.con.commit()
        self.a = self.cur.fetchall()
        return self.a

    def name(self):
        self.cur.execute('SELECT name FROM base')
        self.con.commit()
        self.names = self.cur.fetchall()
        return self.names

    def create(self, value, password):
        self.password = password
        self.value = value
        self.cur.execute('INSERT INTO base(name, password) VALUES(?, ?)', (self.value, self.password, ))
        self.con.commit()



