
"""
Custom error demo

"""
import os
import shutil
from flask import Flask
from sub import divide

# Setting up the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def addition():
    try:
        c = divide(100, 0)
    except Exception as e:
        print(e)
        print(e.code)
        print(e.message)
        return 'error_page_html'

    return str(c)


if __name__ == "__main__":
    app.run(port=500, debug=True)
