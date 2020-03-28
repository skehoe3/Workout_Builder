#flask quickstart guide: export FLASK_APP=hello.py

#if it's not running, its probably because something else is on the port
#use akshay's asnwer here: https://stackoverflow.com/questions/24387451/how-can-i-kill-whatever-process-is-using-port-8080-so-that-i-can-vagrant-up/24388281
#significantly better tutorial: https://code-maven.com/using-templates-in-flask
#the github for the flask tutorial: https://github.com/szabgab/demo-flask-project

from flask import Flask, render_template, request
from src.forms.workout_form import WorkoutForm
from src.workout import Workout

app = Flask(__name__) #create the Flask app
app.config["SECRET_KEY"] = "boom"

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
	"""
	index of the workout builder
	"""
	w = WorkoutForm()
	# if form.validate_on_submit():
	# 	w.build_workout() # TODO: fill this in...
	if request.method == "GET":
		return render_template("index.html", form=w)
	if w.validate_on_submit():
		Workout().build_workout(w.num_ex.data, w.muscle_group.data)
		return render_template("index.html", form=w)
	return "Not implemented"


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

