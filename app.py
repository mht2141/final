####################
# Name : Min-Hua Tsou
# UNI : mht2141
#
# This program serves different webpages depending on what the user has requested.
# The personal homepage has my name, picture, current grade, major, a favorite 
# webiste and links to two other pages on my website.
####################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def homepage():
    return render_template("1006.html") 

@app.route("/jpstatistics")
def attractions():
    return render_template("jpstatistics.html") 

@app.route("/foodinjapan")
def food():
    return render_template("foodinjapanc.html") 


#start the server
if __name__ == "__main__":
    app.run()