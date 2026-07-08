import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    TextField,
    DateTimeField,
)
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

# Pages shown in the nav bar
PAGES = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Timeline", "url": "/timeline"}
]

# Placeholders
ABOUT = [
    {
        "name": "Andrei",
        "description": "Computer Science student at University College Cork, heading into my third year. I enjoy building things, contributing to my college's Claude Society, and exploring new places.",
    },
    {
        "name": "Ghadi",
        "description": "DevOps Engineering student at Polytech Montpellier and a DevOps apprentice at Genvia. I'm passionate about automation, cloud technologies, and cooking in my spare time.",
    },
]

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
        title="MLH Fellow",
        url=os.getenv("URL"),
        pages=PAGES,
        about=ABOUT,
        work_experiences=WORK_EXP,
        education=EDUCATION,
    )


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), pages=PAGES, hobbies=HOBBIES, travel=TRAVEL)


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    timeline_posts = []
    for p in TimelinePost.select().order_by(TimelinePost.created_at.desc()):
        timeline_posts.append(model_to_dict(p))
    return {
        'timeline_posts': timeline_posts
    }


@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    query = TimelinePost.delete().where(TimelinePost.id == post_id)
    rows_deleted = query.execute()

    if rows_deleted == 0:
        return {'error': f'No timeline post with id {post_id}'}, 404

    return {'deleted': post_id}


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title='Timeline', url=os.getenv("URL"), pages=PAGES)
