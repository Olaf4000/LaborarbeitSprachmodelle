from flask import Blueprint, render_template

recommendations_bp = Blueprint('recommendations', __name__)

'''
routes for recommendations
 - recommendations
 - follow up questions
'''

@recommendations_bp.route('/')
def test():
    return render_template('recommendations.html')