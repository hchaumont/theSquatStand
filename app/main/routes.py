from flask import render_template, session, redirect, url_for
from . import main
from .forms import WorkoutInfoForm
from .. import db
from ..models import Workout, Exercise, Entry
from .statistics import WorkoutSummary, createDailyVolumeChart


# Routes
@main.route('/')
def index():
    workouts = Workout.query.all()
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
        session['summary'] = WorkoutSummary(workout)
        return redirect(url_for('.summary'))
    return render_template('log.html', form=form)


@main.route('/summary', methods=['GET', 'POST'])
def summary():
    return render_template('summary.html', summary=session.get('summary'))

@main.route('/stats', methods=['GET'])
def stats():
    orderedWorkouts = Workout.query.order_by('date').all()
    orderedSummaries = [WorkoutSummary(w) for w in orderedWorkouts]
    script, div = createDailyVolumeChart(orderedSummaries)
    return render_template('stats.html', chart_script=script, chart_div=div)
