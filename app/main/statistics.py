import numpy as np
import pandas as pd
from bokeh.plotting import figure

from bokeh.embed import components


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
    p = figure(title='Daily Volume', x_range=days, y_axis_label='Volume')
    p.vbar(x=days, top=dailyVolume['volume'], width=.9)
    return components(p)
