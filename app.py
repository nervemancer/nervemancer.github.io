from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__, template_folder=Path(__name__).parent)


@app.get('/')
def index():
    return render_template('index.html')

