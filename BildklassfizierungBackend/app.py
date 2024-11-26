from flask import Flask, render_template
from routes.test import test_bp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', test="Testvariable")

# Register blueprints
app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(debug=True)