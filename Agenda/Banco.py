import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + "\\agenda.db"

def ConexãoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con
def dql(query):
    vcon = ConexãoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall
    return res
def dml(query):
    try:
        vcon = ConexãoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)