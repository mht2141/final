####################
# Name : Min-Hua Tsou
# UNI : mht2141
#
# This program serves different webpages depending on what the user has requested.
# The index html file displays my name, picture, current grade, major, a favorite 
# webiste and links to two other pages on my website. The foodinjapan html file
# has pictures and descriptions of popular Japanese food. japanstatistics.py 
# modifies a csv file and displays a table of Japan's tourism statistics.
####################

#import statements
import japanstatistics as jp
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/1006")
def python():
    return render_template("1006.html") 

@app.route("/jpstatistics")
def japan_statistics():
    return jp.jpstatistics()

@app.route("/foodinjapan")
def food():
    return render_template("foodinjapan.html") 

#start the server
if __name__ == "__main__":
    app.run()