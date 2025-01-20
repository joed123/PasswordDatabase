from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
from database import db_connector as db
import random
import string

app = Flask(__name__)

db_connection = db.connect_to_database()

mysql = MySQL(app)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "0067"
app.config["MYSQL_DB"] = "securepassDB"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# Routes


def generate_password(uppercase, lowercase, digits, specialchar, length):
    character_pool = ""
    if uppercase:
        character_pool += string.ascii_uppercase
    if lowercase:
        character_pool += string.ascii_lowercase
    if digits:
        character_pool += string.digits
    if specialchar:
        character_pool += string.punctuation

    if not character_pool:  
        return "No characters selected"

    return "".join(random.choice(character_pool) for _ in range(length))


@app.route('/')
def root():
    return render_template("Generate.j2")


@app.route("/search_Login", methods=["POST", "GET"])
def search_login():
    if request.method == "POST":
        username = request.form.get("username")
        
        if username:
            query = "SELECT * FROM Users WHERE username LIKE %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (f"%{username}%",))
            results = cur.fetchall()
    
            if not results:
                return render_template("searchResults.j2", results=None, message="No matching users found.")
            return render_template("searchResults.j2", results=results, message=None)
    
    return render_template("searchLogin.j2")


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


@app.route("/delete_Login", methods=["POST", "GET"])
def delete_user():
    if request.method == "POST":
        username = request.form.get("username")
        
        if not username:  # Check if username is empty
            return render_template("logins.j2", message="Please provide a username to delete.", Users=[])
        
        # Query to delete the user based on the username
        query = "DELETE FROM Users WHERE username = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (username,))
        mysql.connection.commit()
        
        # Check if any row was affected
        if cur.rowcount == 0:
            return render_template("logins.j2", message="No user found with that username.", Users=[])
        
        return redirect("/Logins")
    
    return render_template("deleteLogin.j2")

@app.route('/Categories', methods=["POST", "GET"])
def categories():
    if request.method == "POST":
        if request.form.get("add_Category"):
            category_name = request.form.get("category_name")
            
            if category_name:
                cur = mysql.connection.cursor()
                cur.execute("SELECT password_id FROM passwords LIMIT 1;")
                result = cur.fetchone()

                if result:  # Ensure there is a valid password_id
                    fk_password_id = result["password_id"]
                else:
                    return render_template("Categories.j2", message="No valid password_id found in passwords table.", Password_Categories=[])

                try:
                    query = "INSERT INTO Password_Categories (category_name, FK_password_id) VALUES (%s, %s);"
                    cur.execute(query, (category_name, fk_password_id))
                    mysql.connection.commit()
                    print("Category added successfully!")
                except Exception as e:
                    print(f"Error adding category: {e}")
                    return render_template("Categories.j2", message="Error adding category.", Password_Categories=[])

            return redirect("/Categories")

    elif request.method == "GET":
        query = "SELECT * FROM Password_Categories;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
        return render_template("Categories.j2", Password_Categories=results)

    return render_template("Categories.j2")



@app.route("/edit_Category/<int:id>", methods=["POST", "GET"])
def edit_category(id):
    if request.method == "GET":
        query = "SELECT * FROM Password_Categories WHERE category_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (id,))
        category = cur.fetchone()
        
        if category:
            return render_template("editCategory.j2", category=category)
        else:
            return "Categoryn found", 404

    if request.method == "POST":
        category_name = request.form["category_name"]
        query = "UPDATE Password_Categories SET category_name = %s WHERE category_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (category_name, id))
        mysql.connection.commit()
        return redirect("/Categories")


@app.route("/delete_Category", methods=["POST"])
def delete_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        
        if not category_name:
            return render_template("Categories.j2", message="Please provide a category name to delete.", Password_Categories=[])

        query = "DELETE FROM Password_Categories WHERE category_name = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (category_name,))
        mysql.connection.commit()
        
        if cur.rowcount == 0:
            return render_template("Categories.j2", message="No category found with that name.", Password_Categories=[])
        
        return redirect("/Categories")


@app.route('/Generate', methods=["POST", "GET"])
def generate():
    password_value = ""
    if request.method == "POST":
        uppercase = 'uppercase' in request.form
        lowercase = 'lowercase' in request.form
        digits = 'digits' in request.form
        specialchar = 'specialchar' in request.form
        length = int(request.form.get('length', 8))

        password_value = generate_password(uppercase, lowercase, digits, specialchar, length)
        print(f"Generated Password: {password_value}")

    return render_template("generate.j2", password_value=password_value)


if __name__ == "__main__":

    port = int(os.environ.get('PORT', 13154))
    app.run(port=port, debug=True)
    
