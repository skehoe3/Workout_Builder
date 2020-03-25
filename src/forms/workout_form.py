from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WorkoutForm(FlaskForm):
    """
    Form for our offer page
    """
    num_ex = IntegerField("number of excercises", validators=[DataRequired])
    muscle_group = StringField("muscle group", validators=[DataRequired()])
    submit = SubmitField("Build Workout")
