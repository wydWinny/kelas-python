import sqlite3

con=sqlite3.connect ('./sim.db')

statement ="""
    CREATE TABLE sales(
        cabang TEXT,
        tanggal TEXT,
        penjualan INTEGER,

        PRIMARY KEY (cabang,tanggal)
    );
"""

try:
    cur = con.cursor()
    cur.execute (statement)
    con.commit()
except:
    print (f'failed to create table: {e}')
    
