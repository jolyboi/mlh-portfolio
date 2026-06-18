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

HOBBIES = ["Hobby 1", "Hobby 2", "Hobby 3"]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), pages=PAGES)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), hobbies=HOBBIES)
