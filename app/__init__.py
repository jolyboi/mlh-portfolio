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

TRAVEL = [
    {
        "name": "Ghadi",
        "color": "#1C539F",
        "countries": [
            {"name": "Lebanon", "lat": 33.8547, "lng": 35.8623},
            {"name": "France", "lat": 46.2276, "lng": 2.2137},
            {"name": "Spain", "lat": 40.4637, "lng": -3.7492},
            {"name": "Turkey", "lat": 38.9637, "lng": 35.2433},
            {"name": "Switzerland", "lat": 46.8182, "lng": 8.2275},
        ],
    },
    {
        "name": "Andrei",
        "color": "#e74c3c",
        "countries": [
            {"name": "Ireland", "lat": 53.1424, "lng": -7.6921},
            {"name": "UK", "lat": 55.3781, "lng": -3.4360},
            {"name": "Singapore", "lat": 1.3521, "lng": 103.8198},
            {"name": "Egypt", "lat": 26.8206, "lng": 30.8025},
            {"name": "Serbia", "lat": 44.0165, "lng": 21.0059},
        ],
    },
]


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellows",
        url=os.getenv("URL"),
        pages=PAGES,
        work_experiences=WORK_EXP,
        education=EDUCATION,
    )


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), pages=PAGES, hobbies=HOBBIES, travel=TRAVEL)

