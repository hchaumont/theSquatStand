from flask import render_template, session, redirect, url_for
from . import main
from .forms import WorkoutInfoForm
from .. import db
from ..models import Workout, Exercise, Entry


# Routes
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/log', methods=['GET', 'POST'])
def log():
    workout = Workout()
    exercise = Exercise()
    entry = Entry()
    exercise.entries = [entry]
    workout.exercises = [exercise]
    form = WorkoutInfoForm(obj=workout)

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['date'] = form.date.data
        session['exercises'] = form.exercises.data
        session['notes'] = form.notes.data
        form.populate_obj(workout)
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('.summary'))
    return render_template('log.html', form=form)


@main.route('/summary', methods=['GET', 'POST'])
def summary():
    return render_template('summary.html', name=session.get('name'),
                           date=session.get('date'),
                           notes=session.get('notes'), exercises=session.get('exercises'))
