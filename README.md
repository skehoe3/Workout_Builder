# Read Me

# What does this do?
You input 1 of several muscle groups (core, cardio, lower body, or upper body) and the desired number of excercises for that group.  The code will randomly select the specified number of excercise for that group, assign a duration (in seconds), and then read it aloud and count down for you.

# Prerequisites
To run this code, you'll need to have the following installed: 

- python3
- numpy
- time
- random
- pyttsx3

This is a fairly basic formulation so far, but additional features are envisioned.

# Additional Features
- web UI
- video/gif showing how to do the excercise
- pause functionality
- save to favorites
    - the single excercise
    - the full workout that was built

# Running the App
Execute the following code in terminal from the Workout_Builder folder:

export FLASK_APP=hello.py
flask run

if running on MacOS, be sure to install ffmpeg via brew install ffmpeg