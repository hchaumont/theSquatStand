from . import db


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
        return '<{}>'.format(self.exname)


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    def __repr__(self):
        return '<{} x {} reps x {} sets>'.format(self.weight, self.reps, self.sets)
