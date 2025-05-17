from flask import Flask, request

app = Flask(__name__)

app.route('/', methods = ['GET'])
def default():
    return "siap"

if __name__ == "__main__":
    print("Starting server ...")
    port ="9999"
    app.run(host='0.0.0.0', port=port, threaded=True, )
