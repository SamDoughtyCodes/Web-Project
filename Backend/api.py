from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # Set up the app section of the program

# Enforce rules on connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # What sites can access (the host of the website)
    allow_credentials=True,
    allow_methods=["*"],  # What requests (e.g. GET, POST) can be accepted, * represents all
    allow_headers=["*"],
)

# Requests ending "/api/test" will call this function, which returns PlainText
@app.get("/api/test", response_class=PlainTextResponse)
def test_func():
    return "Holy crap this actually works!"