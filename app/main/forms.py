from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, FloatField, FieldList
from wtforms import TextAreaField, IntegerField, FormField
from wtforms import Form as NoCsrfForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from ..models import Entry, Exercise


class SetForm(NoCsrfForm):
    weight = FloatField('Weight')
    reps = IntegerField('Reps')
    sets = IntegerField('Sets')


class ExerciseForm(NoCsrfForm):
    exname = StringField('Exercise Name')
    entries = FieldList(FormField(SetForm, default=lambda: Entry()), min_entries=1)


class WorkoutInfoForm(FlaskForm):
    name = StringField('Workout Name:', default='Workout',
                       validators=[DataRequired()])
    date = DateField('Workout Date:')
    # time = TimeField('Workout Time')
    notes = TextAreaField('Workout Notes:')
    exercises = FieldList(FormField(ExerciseForm, default=lambda: Exercise()), min_entries=1)
    submit = SubmitField('Submit')
