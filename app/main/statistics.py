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
    p = figure(x_axis_type='datetime')
    p.vbar(x=dailyVolume['date'], top=dailyVolume['volume'], width=1)
    return components(p)
