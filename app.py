from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db
app = Flask(__name__)

db_connection = db.connect_to_database()

mysql = MySQL(app)
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_lyand"
app.config["MYSQL_PASSWORD"] = "3318"
app.config["MYSQL_DB"] = "cs340_lyand"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# Routes
@app.route('/')
def root():
    return render_template("Generate.j2")

@app.route('/Logins', methods=["POST", "GET"])
def Users():
    if request.method == "POST":
        if request.form.get("add_User"):
            email = request.form["email"]
            username = request.form["username"]
            if len(email)>1:
                query = "INSERT INTO Users (email, username) VALUES (%s, %s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (email, username))
                mysql.connection.commit()

            return redirect("/Logins")

    elif request.method == "GET":
        query = "SELECT * FROM Users;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("Logins.j2", Users=results)

@app.route("/edit_Login/<int:id>", methods=["POST", "GET"])
def edit_people(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Users WHERE user_id = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("editLogin.j2", Users=data)

    if request.method == "POST":
        if request.form.get("add_User"):
            email = request.form["email"]
            username = request.form["username"]
            if len(email)>1:
                query = "UPDATE Users SET Users.email = %s, Users.username = %s WHERE Users.user_id = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (email, username))
                mysql.connection.commit()

            return redirect("/Logins")


@app.route("/delete_Login/<int:id>")
def delete_user(id):
    query = "DELETE FROM Users WHERE user_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    return redirect("/Logins")

@app.route('/Categories', methods=["POST", "GET"])
def categories():
    if request.method == "POST":
        if request.form.get("add_Category"):
            category_name = request.form["email"]
            if len(category_name) > 0:
                query = "INSERT INTO Password_Categories (category_name) VALUES (%s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (category_name))
                mysql.connection.commit()

            return redirect("/Categories")

    elif request.method == "GET":
        query = "SELECT * FROM Password_Categories;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("Categories.j2", categories=results)
    
    return render_template("Categories.j2")

@app.route('/History')
def history():
    return render_template("History.j2")

@app.route('/Generate')
def generate():
    return render_template("Generate.j2")

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    port = int(os.environ.get('PORT', 13154))
    app.run(port=port, debug=True)
    
