import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv
from database.db_credentials import host, user, passwd, db

# Load our environment variables from the .env file in the root of our project.
load_dotenv(find_dotenv())


def connect_to_database():
    '''
    connects to a database and returns a database objects
    '''
    db_connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    return db_connection


def execute_query(db_connection = None, query = None, query_params = ()):

    if db_connection is None:
        print("No connection to the database found! Have you called connect_to_database() first?")
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params));
    cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute(query, query_params)

    db_connection.commit();
    return cursor


if __name__ == '__main__':
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db = connect_to_database()
    query = "SELECT * from bsg_people;"
    results = execute_query(db, query);
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)
