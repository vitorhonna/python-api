from flask import Flask, jsonify, request, send_file

app = Flask(__name__)


@app.route('/my-first-api', methods=['GET'])
def hello():
    return jsonify({"message": "Hello world!"})


@app.route('/hello', methods=['GET'])
def hello_user():
    name = request.args.get('name')
    if name is None:
        text = 'Hello!'
    else:
        text = f'Hello, {name}!'
    return jsonify({"message": text})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
