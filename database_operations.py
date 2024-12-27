import sqlite3

# Establish the database connection
con = sqlite3.connect('sql_data.db')

# CRUD Operations
def insertData(name, age, city):
    qry = "INSERT INTO user (NAME, AGE, CITY) VALUES (?, ?, ?);"
    con.execute(qry, (name, age, city))
    con.commit()
    print("User Details Added...")

def updateData(name, age, city, id):
    qry = "UPDATE user SET NAME=?, AGE=?, CITY=? WHERE ID=?;"
    con.execute(qry, (name, age, city, id))
    con.commit()
    print("User Details Updated...")

def deleteData(id):
    qry = "DELETE FROM user WHERE ID=?;"
    con.execute(qry, (id,))
    con.commit()
    print("Deleted...")

def selectData():
    qry = "SELECT * FROM user;"
    result = con.execute(qry)
    return list(result)  # Return results instead of printing directly

def createTable():
    qry = """
    CREATE TABLE IF NOT EXISTS user (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INTEGER NOT NULL,
        CITY TEXT NOT NULL
    );
    """
    con.execute(qry)
    con.commit()
    print("Table Created")

