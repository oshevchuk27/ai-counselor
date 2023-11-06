from flask import flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_goals():
    return jsonify({"Hello":"World"})



if __name__ == '__main__':
    app.run(debug=True)