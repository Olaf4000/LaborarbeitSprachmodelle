import os
import sqlite3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.cli import load_dotenv

from FlaskApp.api.api import api_bp
from routes.test import test_bp
from routes.diagnosis import diagnosis_bp
from routes.recommendations import recommendations_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'jgagnj<ngjpnhnbmbnshnowkrhnsmba25uo11o'

# Konfiguration für die SQLite-Datenbank
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisiere SQLAlchemy
db = SQLAlchemy(app)

# Definiere die Modelle
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    symptoms = db.Column(db.String(255), nullable=False)

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', back_populates="diagnoses")

User.diagnoses = db.relationship('Diagnosis', order_by=Diagnosis.id, back_populates="user")

# Stelle sicher, dass alle Datenbanktabellen erstellt werden
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html', test="Testvariable")

# Register blueprints
app.register_blueprint(test_bp, url_prefix='/subpage')
app.register_blueprint(diagnosis_bp, url_prefix='/diagnosis')
app.register_blueprint(recommendations_bp, url_prefix='/recommendations')
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)