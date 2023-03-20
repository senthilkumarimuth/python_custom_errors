
"""
Custom error demo

"""
import os
import shutil
from flask import Flask, render_template, abort
from sub import divide
from custom_errors import CustomZeroDivision
# Setting up the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def addition():
    try:
      c = divide(100, 0)
    except CustomZeroDivision as cs:
        abort(503)

    return str(c)


# Handling error 404 and displaying relevant web page
@app.errorhandler(503)
def not_found_error(cs):
    return render_template('503.html'), 503


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(port=500, debug=False)
