from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, FloatField, FieldList
from wtforms import TextAreaField, IntegerField, FormField
from wtforms import Form as NoCsrfForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'herp derp'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)


# Database Models
class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.DateTime)
    notes = db.Column(db.Text)
    exercises = db.relationship('Exercise', backref='workout')

    def __repr__(self):
        return '<{} on {}>'.format(self.name, self.date)


class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    exname = db.Column(db.String)
    entries = db.relationship('Entry', backref='exercise')
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))

    def __repr__(self):
        return '<{}: {}x{}>'.format(self.name, self.weight, self.reps)


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    sets = db.Column()
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))


# Forms
class SetForm(NoCsrfForm):
    weight = FloatField('Weight')
    reps = IntegerField('Reps')
    sets = IntegerField('Sets')


class ExerciseForm(NoCsrfForm):
    exname = StringField('Exercise Name')
    entries = FieldList(FormField(SetForm), min_entries=1)


class WorkoutInfoForm(FlaskForm):
    name = StringField('Workout Name:', default='Workout',
                       validators=[DataRequired()])
    date = DateField('Workout Date:')
    # time = TimeField('Workout Time')
    notes = TextAreaField('Workout Notes:')
    exercises = FieldList(FormField(ExerciseForm), min_entries=1)
    submit = SubmitField('Submit')


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/log', methods=['GET', 'POST'])
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
        db.session.commit()
        return redirect(url_for('summary'))
    return render_template('log.html', form=form)


@app.route('/summary', methods=['GET', 'POST'])
def summary():
    return render_template('summary.html', name=session.get('name'),
                           date=session.get('date'),
                           notes=session.get('notes'), exercises=session.get('exercises'))


# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
