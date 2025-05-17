from flask import Flask, request, render_template
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    f = open('index.html', 'r')
    return f.read()

@app.route('/index.html')
def index2():
    f = open('index.html', 'r')
    return f.read()

@app.route('/entry.html')
def entry():
    f = open('entry.html', 'r')
    return f.read()

@app.route('/hapus.html')
def hapus():
    f = open('hapus.html', 'r')
    return f.read()

@app.route ('/tambahdata')
def tambahdata():
    params = request.args
    nama = params.get('nama', None)
    umur = params.get('umur', None)
    kota = params.get('kota', None)

    f = open('karyawan.csv', 'a')
    f.write(nama + ',' + umur + ',' + kota +'\n')
    f.close()
    g = open('entry.html', 'r')
    return g.read()

@app.route('/updatedata')
def updatedata():
    params = request.args
    nama = params.get('nama', None)
    umur = params.get('umur', None)

    f = open('karyawan.csv', 'r')
    csv_text = f.read()
    f.close()
    rows = csv_text.split('\n')[0:-1]
    
    f = open('karyawan.csv', 'w')
    for row in rows:
        row_data = row.split(',')
        nama_row = row_data[0]
        usia_row = row_data[1]
        kota_row = row_data[2]
        if(nama != nama_row):
            print(nama, 'tidak sama dengan',nama_row)
            f.write(nama_row + ',' + usia_row + ',' + kota_row +'\n')
        else:
            f.write(nama_row + ',' + umur + ',' + kota_row +'\n')
    f.close()
    return f'nama {nama} sudah terupdate'


@app.route('/deletedata')
def deletedata():
    params = request.args
    nama = params.get('nama', None)

    f = open('karyawan.csv', 'r')
    csv_text = f.read()
    f.close()
    rows = csv_text.split('\n')[0:-1]
    
    f = open('karyawan.csv', 'w')
    for row in rows:
        row_data = row.split(',')
        nama_row = row_data[0]
        usia_row = row_data[1]
        kota_row = row_data[2]
        if(nama != nama_row):
            print(nama, 'tidak sama dengan',nama_row)
            f.write(nama_row + ',' + usia_row + ',' + kota_row +'\n')
        else:
            print(nama, 'sama', nama_row)
    f.close()

    return (nama)

   

@app.route('/report.html')
def report():
   data = pd.read_csv('karyawan.csv')
   resp = render_template('table.html', tables=[data.to_html()], titles=['']) 
   return resp

app.run(debug=True)