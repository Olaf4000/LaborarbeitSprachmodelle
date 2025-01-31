from flask import Flask, render_template

from api.api_controller import api_bp
from routes.diagnosis import diagnosis_bp
from routes.doctors import doctors_bp

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for session management and security
app.secret_key = 'jgagnj<ngjpnhnbmbnshnowkrhnsmba25uo11o'


@app.route('/')
def home():
    """
    Renders the home page (index.html).

    Returns:
        Rendered HTML page for the home page.
    """
    return render_template('index.html')


# Register blueprints for different routes
# Blueprint for doctors-related routes
app.register_blueprint(doctors_bp, url_prefix='/doctors')
# Blueprint for diagnosis-related routes
app.register_blueprint(diagnosis_bp, url_prefix='/diagnosis')
# Blueprint for API-related routes
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)