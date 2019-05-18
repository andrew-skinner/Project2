from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo


#instance of Flask
app = Flask(__name__)
data = 
# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    #print("THIS IS WHERE YOUR PRINT STMNT IS")
    #print(data)
    # Return template and data
    return render_template("main.html", data=data)

@app.route("/energyvsc02")
def c02():

    return render_template("1.html", data=data)

@app.route("/typeoffuel")
def type():

    return render_template("2.html", data=data)

@app.route("/heatmap")
def map():

    return render_template("3.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)