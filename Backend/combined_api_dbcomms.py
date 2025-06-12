from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import connect

# Create class to store a form submission object
class FormSubmission():
    user: str
    passw: str

app = FastAPI()  # Set up the app section of the program

# Enforce rules on connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # What sites can access (the host of the website)
    allow_credentials=True,
    allow_methods=["*"],  # What requests (e.g. GET, POST) can be accepted, * represents all
    allow_headers=["*"],
)

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

# Request which sends a fixed query to the server for testing, responding with a JSON object
@app.get("/api/test_db")
def test_db_conn():
    set_db("School")
    result = run_query("SELECT * FROM subjects")
    return result

# Request which sends user and password data
@app.post("api/test_post")
def test_post(data: FormSubmission):
    pass  # TODO: Make this function