####################
# Name : Min-Hua Tsou
# UNI : mht2141
#
# 
####################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    return render_template("index.html")

@app.route("/1006")
def test123():
    #return "<p>This is my <b>1006</b> website! </p>"
    return render_template("1006.html")

#start the server
if __name__ == "__main__":
    app.run()