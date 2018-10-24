from flask import render_template, session, redirect, url_for
from . import main
from .forms import WorkoutInfoForm
from .. import db
from ..models import Workout, Exercise, Entry
from .statistics import WorkoutSummary, createDailyCharts, createPRList
from sqlalchemy import desc

# Routes
@main.route('/')
def index():
    workouts = Workout.query.order_by(desc('date')).all()
    workout_summaries = [WorkoutSummary(workout) for workout in workouts]
    return render_template('index.html', workouts=workouts, workout_summaries=workout_summaries)


@main.route('/log', methods=['GET', 'POST'])
def log():
    workout = Workout()
    exercise = Exercise()
    entry = Entry()
    exercise.entries = [entry]
    workout.exercises = [exercise]
    form = WorkoutInfoForm(obj=workout)

    if form.validate_on_submit():
        form.populate_obj(workout)
        db.session.add(workout)
        db.session.commit()
        session['workout_id'] = workout.id
        return redirect(url_for('.summary'))
    return render_template('log.html', form=form)


@main.route('/summary', methods=['GET', 'POST'])
def summary():
    workout_id = session.get('workout_id')
    summary = WorkoutSummary(Workout.query.filter(Workout.id == workout_id).first())
    return render_template('summary.html', summary=summary)


@main.route('/edit/<workout_id>', methods=['GET', 'POST'])
def edit(workout_id):
    workout = Workout.query.filter(Workout.id == workout_id).first()
    form = WorkoutInfoForm(obj=workout)

    if form.validate_on_submit():
        form.populate_obj(workout)
        db.session.commit()
        session['workout_id'] = workout.id
        return redirect(url_for('.summary'))
    return render_template('log.html', form=form)


@main.route('/stats', methods=['GET'])
def stats():
    orderedWorkouts = Workout.query.order_by('date').all()
    orderedSummaries = [WorkoutSummary(w) for w in orderedWorkouts]
    charts = createDailyCharts(orderedSummaries)
    PRList = createPRList()
    return render_template('stats.html', charts=charts, PRList=PRList)
