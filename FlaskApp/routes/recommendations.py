from flask import Blueprint, render_template, session

recommendations_bp = Blueprint('recommendations', __name__)

'''
routes for recommendations
 - recommendations
 - follow up questions
'''

@recommendations_bp.route('/')
def recommendations():

    return render_template('recommendations.html')