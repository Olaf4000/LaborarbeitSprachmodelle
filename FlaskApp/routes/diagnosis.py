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
    from FlaskApp.app import db, User, Diagnosis  # Importiere hier, um zirkuläre Importe zu verhindern

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

    # Todo --> es funktioniert noch nicht und try catch ist nur das die App nicht abstürzt
    # Erstelle einen neuen User
    try:
        new_user = User(age=session['age'], gender=session['gender'], symptoms=session['symptoms'])
        db.session.add(new_user)
        db.session.commit()  # Speichern des Users
    except Exception as e:
        db.session.rollback()
        flash(f'Fehler beim Speichern des Users: {str(e)}', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    # Todo --> es funktioniert noch nicht und try catch ist nur das die App nicht abstürzt
    # Optional: Diagnose hinzufügen
    try:
        diagnosis_text = "Diagnose basierend auf den Symptomen"
        new_diagnosis = Diagnosis(user_id=new_user.id, diagnosis=diagnosis_text)
        db.session.add(new_diagnosis)
        db.session.commit()  # Speichern der Diagnose
    except Exception as e:
        db.session.rollback()
        flash(f'Fehler beim Speichern der Diagnose: {str(e)}', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    #session['diagnosis'] = ...  # API Aufruf
    time.sleep(3)

    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results')
def results():

    return render_template('diagnosis.html', mode='results_diagnosis')