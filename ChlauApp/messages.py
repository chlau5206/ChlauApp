from flask import Flask, render_template
import sqlite3


# Database configuration (adjust as needed)
DATABASE = 'your_database.db'  # Path to your SQLite database file

def get_db():
    db = getattr(g, '_database', None) #Check if db is already open.
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Example route
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()

    # Fetch data from the database (example query)
    cursor.execute("SELECT id, name, value FROM my_table") # Replace with your query
    data = cursor.fetchall()

    return render_template('index.html', data=data)

