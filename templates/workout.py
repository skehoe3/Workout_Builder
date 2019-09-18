from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class Workout(Form):
    """Form for round1.py"""
    muscleGroup = StringField('Muscle Group', [validators=DataRequired(message=()"gettin' swole"))])
    numEx = IntegerField('Number of Excercises', [validators=DataRequired(message=()"how swole?"))])
