#
# main.py
#

# imports
from flask import Flask
import os

# configuration
DEBUG = int(os.environ["DEBUG"])

app = Flask(__name__)
app.debug = bool(DEBUG)

if __name__ == "__main__":
    app.run()

import views
