from flask import Flask, render_template, request, redirect
import sqlite3
# request.args used with only GET request
#request.form used with the POST request

app = Flask(__name__)
#A db variable that opens the file(test.db)
db = SQL("sqlite:///test.db")

#Defining the only sports supported in the app
SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

#Dictionary to store the registrants in
#REGISTRANTS = {}
# Default route
@app.route("/")
def index():
    return render_template("index.html", sports = SPORTS)


@app.route("/register", methods = ["POST"])
def register():
    #Getting the users name from the form and save it to name
    name = request.form.get("name")
    #Getting the sports name and save it in sports variable
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("faliure.html")
    #sending registrants data into the db
    db.execute("INSERT INTO REGISTRANTS(name, sport) VALUES(?,?)", name, sport)
    
    #confirm registration
    return redirect("/registrants")
    
    #indexing to the dictionary using the name and set it to sport
    #REGISTRANTS[name] = sport
#another route to show all the registrants
@app.route("/registrants")
def registrants():
    #return a html file and pass in the registrants 
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants =registrants)