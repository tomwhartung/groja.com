""" Ye olde hello world sanity check, using only the base template.

Purpose: ensure we can process the request to render a simple template
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    Chapter 3 of the "Flask Web Development" book (M.Grinberg 2014)
Usage:
    bin/hello-run.sh
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    """ Say "hello" by rendering the hello.html template """
    return render_template('hello.html')

#
# Run the app!
#
if __name__ == '__main__':
    app.run(debug=True)

