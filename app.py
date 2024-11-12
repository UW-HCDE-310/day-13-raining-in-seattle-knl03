import urllib.request
def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return("True")
    else:
        return("False")

#print(is_it_raining_in_seattle())

from flask import Flask

day13 = Flask(__name__)

@day13.route("/")
def index():
    return is_it_raining_in_seattle()