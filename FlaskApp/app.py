import os
import sqlite3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.cli import load_dotenv

from api.api_controller import api_bp
from routes.test import test_bp
from routes.diagnosis import diagnosis_bp
from routes.recommendations import recommendations_bp
from routes.doctors import doctors_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'jgagnj<ngjpnhnbmbnshnowkrhnsmba25uo11o'

@app.route('/')
def home():
    return render_template('index.html')

# Register blueprints
app.register_blueprint(doctors_bp, url_prefix='/doctors')
app.register_blueprint(test_bp, url_prefix='/subpage')
app.register_blueprint(diagnosis_bp, url_prefix='/diagnosis')
app.register_blueprint(recommendations_bp, url_prefix='/recommendations')
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)