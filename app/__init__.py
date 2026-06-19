import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Pages shown in the nav bar
PAGES = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"}
]

# Placeholders
WORK_EXP = [
    {
        "name": "Andrei",
        "entries": [
            {"title": "Claude Soc's Tutor", "dates": "Apr 2026 - Present", "description": "Do workshops and organize events"},
        ],
    },
    {
        "name": "Ghadi",
        "entries": [
            {"title": "Genvia", "dates": "Oct 2025 - Aug 2026", "description": "DevOps Apprentice"},
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
                "dates": "2024-2028",
                "description": "Currently going into the 3rd year.",
            },
        ],
    },
    {
        "name": "Ghadi",
        "entries": [
            {
                "title": "M.Eng Devops Engineering",
                "subtitle": "Polytech Montpellier",
                "dates": "2025-2028",
                "description": "A CS degree centered around DevOps technologies and methodoligies",
            },
        ],
    },
]

HOBBIES = ["Hobby 1", "Hobby 2", "Hobby 3"]


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
  
  
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), hobbies=HOBBIES)

