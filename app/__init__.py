import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Pages shown in the nav bar
PAGES = [
    {"name": "Home", "url": "/"}
]

# Placeholders
WORK_EXP = [
    {
        "name": "Andrei",
        "entries": [
            {"title": "Insert Info", "dates": "Insert Info", "description": "Placeholder"},
        ],
    },
    {
        "name": "Ghadi",
        "entries": [
            {"title": "Insert Info", "dates": "Insert Info", "description": "Placeholder"},
        ],
    },
]

EDUCATION = [
    {
        "name": "Andrei",
        "entries": [
            {
                "title": "BSc Computer Science",
                "subtitle": "University College Cork",
                "dates": "2024 – 2028",
                "description": "Placeholder",
            },
        ],
    },
    {
        "name": "Ghadi",
        "entries": [
            {
                "title": "Insert Info",
                "subtitle": "Insert Info",
                "dates": "Insert Info",
                "description": "Placeholder",
            },
        ],
    },
]

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="MLH Fellow", 
        url=os.getenv("URL"), 
        pages=PAGES,
        work_experiences=WORK_EXP,
        education=EDUCATION,
    )
