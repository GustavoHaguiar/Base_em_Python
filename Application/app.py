from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'