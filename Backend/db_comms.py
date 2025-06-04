from mysql.connector import connect

# Connect to the server
db = connect(
    host="localhost",
    user="py_script",
    password="py_db_050722"
)

cursor = db.cursor()

def set_db(db_name: str):
    """
    Function to set the in use database

    param db_name: The name of the database to set.
    """
    query = "USE " + db_name + ";"
    cursor.execute(query)

def run_query(query: str):
    """
    Function to send and run a query and return the result

    param query: the SQL query to run
    returns result: the result of the SQL query
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Testing
if __name__ == "__main__":
    set_db("school")
    x = run_query("SELECT * FROM subjects")
    print(x)