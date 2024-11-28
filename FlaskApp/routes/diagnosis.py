from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time

diagnosis_bp = Blueprint('diagnosis', __name__)

'''
routes for diagnosis
 - symptoms input
 - diagnosis output
'''

@diagnosis_bp.route('/')
def diagnosis():

    return render_template('diagnosis.html', mode='home_diagnosis')

@diagnosis_bp.route('/submit_diagnosis', methods=['POST'])
def submit_diagnosis():
    if not request.form['age'].isdigit():
        flash('Please enter a valid age', 'error')
        return redirect(url_for('diagnosis.diagnosis'))
    elif request.form['symptoms'].strip() == '':
        flash('Please enter a symptom description', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    session['age'] = request.form['age']
    session['gender'] = request.form['gender']
    session['symptoms'] = request.form['symptoms']

    print(session.get('age'), session.get('gender'), session.get('symptoms'))

    #session['diagnosis'] = ...  # API Aufruf
    time.sleep(3)

    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results')
def results():

    return render_template('diagnosis.html', mode='results_diagnosis')