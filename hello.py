#flask quickstart guide: export FLASK_APP=hello.py

#if it's not running, its probably because something else is on the port
#use akshay's asnwer here: https://stackoverflow.com/questions/24387451/how-can-i-kill-whatever-process-is-using-port-8080-so-that-i-can-vagrant-up/24388281
#significantly better tutorial: https://code-maven.com/using-templates-in-flask
#the github for the flask tutorial: https://github.com/szabgab/demo-flask-project

from flask import Flask, render_template, request
from round1 import Workout

app = Flask(__name__) #create the Flask app

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
	print('testing1')
	w = Workout()
	if request.method == 'POST': #this block is only entered when the form is submitted
		print("testing2")
		ex = request.form.get('ex')
		group = request.form['group']
		return '''
				  <h1>Workout Builder</h1>
				  <p>Build your own workout! Choose any number of excercises you'd like, and from upper body, lower body
				  , core, or cardio excercise types</p>
				  <h2>Number of Excercises: {}</h2>
                  <h2>Muscle Group:{}</h2>'''.format(ex, group)
	print('testing3')
	return '''<form method="POST">
                  Number of Excercises:: <input type="text" name="ex"><br>
                  Muscle Group: <input type="text" name="group"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

