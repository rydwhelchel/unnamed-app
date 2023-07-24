from flask import Flask, make_response, request
from flask_cors import CORS
from counter import Counter


app = Flask(__name__)
CORS(app)

counter = Counter()


@app.route("/api/hello")
def hello_world():
    return "<h1>Hello World!</h1>"


@app.route("/api/save-counter", methods=["POST"])
def save_counter():
    num = request.json
    app.logger.info(f"Saving {num}")
    app.logger.info(f"Clicker is now at {counter.load_counter()}")
    counter.add_to_counter(num)
    success_string = f"<h1>Successfully added {num} to counter and saved</h1>"
    response = {"response": success_string}
    return make_response(response, 200)


@app.route("/api/load-counter", methods=["GET"])
def load_counter():
    return f"<h1>The counter is {counter.load_counter()}</h1>"
