from flask import Flask, render_template

from routes.test import test_bp
from routes.diagnosis import diagnosis_bp
from routes.recommendations import recommendations_bp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', test="Testvariable")

# Register blueprints
app.register_blueprint(test_bp, url_prefix='/subpage')
app.register_blueprint(diagnosis_bp, url_prefix='/diagnosis')
app.register_blueprint(recommendations_bp, url_prefix='/recommendations')

if __name__ == '__main__':
    app.run(debug=True)