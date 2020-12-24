# pip install flask
# url : http://127.0.0.1:8080/api

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

data = {
    "str" : "Hello, World!",
    "int" : 12,
    "float" : 12.5,
    "array" : [1,"2","3",4]
}

@app.route('/api')
def api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
