import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from ..models import db, Exercise, Entry

class ExerciseSummary:
    def __init__(self, exercise):
        self.exname = exercise.exname
        self.reps = sum(entry.reps * entry.sets for entry in exercise.entries)
        self.volume = sum(entry.weight * entry.reps * entry.sets for entry in exercise.entries)
        self.entries = exercise.entries


class WorkoutSummary:
    def __init__(self, workout):
        self.id = workout.id
        self.name = workout.name
        self.date = workout.date
        self.notes = workout.notes
        self.exercises = [ExerciseSummary(exercise) for exercise in workout.exercises]
        self.reps = sum(exercise.reps for exercise in self.exercises)
        self.volume = sum(exercise.volume for exercise in self.exercises)


def createDailyVolumeChart(workoutSummaryList):
    df = pd.DataFrame([{'date': w.date, 'volume': w.volume} for w in workoutSummaryList])
    dailyVolume = df.groupby('date').sum()
    days = [str(d).split()[0] for d in dailyVolume.index]
    p = figure(title='Daily Volume', x_range=days, y_axis_label='Volume (lbs.)', height=300,
               sizing_mode='scale_width')
    p.vbar(x=days, top=dailyVolume['volume'], width=.9)
    return components(p)


def createDailyCharts(workoutSummaryList):
    df = pd.DataFrame([{'date': w.date, 'volume': w.volume, 'reps': w.reps} for w in workoutSummaryList])
    dailyVolume = df.groupby('date').sum()
    days = [str(d).split()[0] for d in dailyVolume.index]
    p = figure(title='Daily Volume', x_range=days, y_axis_label='Volume', 
               height=300, sizing_mode='scale_width')
    p.vbar(x=days, top=dailyVolume['volume'], width=.9)
    q = figure(title='Daily Reps', x_range=days, y_axis_label='Reps',
               height=300, sizing_mode='scale_width')
    q.vbar(x=days, top=dailyVolume['reps'], width=.9)
    return [components(p), components(q)]

def getPR(exname):
    exlist = Exercise.query.filter(Exercise.exname == exname).all()
    PR = 0
    for e in exlist:
        PR = max(PR, max(ent.weight for ent in e.entries))
    return PR


def createPRList():
    exnames = set(e[0] for e in db.session.query(Exercise.exname).all())
    return [{'name': exname, 'weight': getPR(exname)} for exname in sorted(exnames)]
