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
	if request.method == "GET":
		return render_template("index.html", form=w)
	if request.method == "POST":
		Workout().build_workout(w.num_ex.data, w.muscle_group.data)
		return render_template("index.html", form=w)
	return "Not implemented"


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

