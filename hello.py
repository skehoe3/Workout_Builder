#flask quickstart guide: export FLASK_APP=hello.py

#if it's not running, its probably because something else is on the port
#use akshay's asnwer here: https://stackoverflow.com/questions/24387451/how-can-i-kill-whatever-process-is-using-port-8080-so-that-i-can-vagrant-up/24388281
#significantly better tutorial: https://code-maven.com/using-templates-in-flask
#the github for the flask tutorial: https://github.com/szabgab/demo-flask-project

from flask import Flask, render_template, request
import round1

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    #text = request.form['text']
    #processed_text = text.lower()
    #return processed_text
	print(request.form.get('muscleGroup'))

if __name__ == '__main__':
	#ONLY USE FOR DEV PURPOSES
	#using otherwise essentially makes your pc easily hacked
	#-------
	#use ctrl + shift + r to reload the page AND clear the cache-- this
	#is important if you want to see your chagnes rendered!!!
	#-------
	debug = True #when this is true, flask continually monitors the file for changes
	FLASK_ENV=development
	TEMPLATES_AUTO_RELOAD=True
	app.run()

