import sqlite3

con = sqlite3.connect('karyawan.db')
statement = """
    DELETE FROM karyawan
    WHERE nama = ?;
"""

nama = 'alven'
cur = con.cursor()
rows = cur.execute(statement, (nama,))
print(rows.rowcount)
con.commit()