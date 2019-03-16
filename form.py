from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class workoutForm(FlaskForm):
	muscleGroup = StringField('Muscle Group', validators=[DataRequired()])
    numExcercises = PasswordField('Number of Excercises', validators=[DataRequired()])
    submit = SubmitField('Submit')