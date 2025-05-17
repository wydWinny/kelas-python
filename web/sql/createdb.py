import sqlite3

con = sqlite3.connect('karyawan.db')
statement = """
    CREATE TABLE karyawan (
        id INTEGER,
        nama TEXT,
        umur INTEGER,
        kota TEXT
    );
"""

cur = con.cursor()
cur.execute(statement)
con.commit()