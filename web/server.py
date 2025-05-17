from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    return "kembalikan sebuah text"

@app.route('/index.html')
def serve_index():
    f = open('index.html', 'rb')
    return f.read()

@app.route('/table.html')
def serve_table():
    f = open('table.html', 'rb')
    return f.read()

@app.route('/entry.html')
def serve_entry():
    f = open('entry.html', 'rb')
    return f.read()

@app.route('/home/winny/belajar/web/ikkan.jpg')
def serve_ikan():
    f = open('/home/winny/belajar/web/ikkan.jpg', 'rb')
    return f.read()

@app.route('/process')
def process():
    request_masuk = request.args
    return request_masuk

@app.route('/tuliscsv', methods = ['GET', 'POST'])
def tulis_csv():
    req_params = dict(request.args)

    csv_file = open('berkas.csv','a')
    #csv_file.write("nama,umur\n")
    csv_file.write(f'{req_params["formname"]}, {req_params["formumur"]}\n')
    csv_file.close()

    f =  open('entry.html', 'r')
    return f.read()
    # return "berhasil ditulis"

@app.route('/table2')
def table2():
    data = pd.read_csv('berkas.csv')
    print(data.to_html())
    resp = render_template('template.html', tables=[data.to_html()], titles=[''])
    return resp

if __name__ == "__main__":
    print("Starting server ...")
    port ="5000"
    app.run(debug=True)


