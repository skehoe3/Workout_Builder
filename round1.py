import numpy as np
import pyttsx3 as pt
from random import randint
import time
import abc


class Workout():
	#randomly selects the number of excercises specified from the muscle group desired.
	#reorg the muscle groups as dictionaries. put it in a resources file.
	def _build_component(self, num_excercises, musc_group = ['upper_body', 'lower_body', 'core', 'cardio']):
		if 	musc_group == 'upper_body':
			ex_type = ['Normal Pushups','tricep dip', 'plank up', 'inchworm', 'plank taps', 'lateral plank walks', 'plank jacks']
		elif musc_group == 'lower_body':
			ex_type = ['lunges', 'reverse lunges', 'squats', 'Plié Squat Calf Raises', 'side lunges', 'single leg raises', 'side leg raises', 'inner leg raises']
		elif musc_group == 'core':
			ex_type == ['shoulder taps', 'simple plank', 'plank with knee taps', 'plank and hip twists', 'plank and knee swings', 'flutter kicks', 'bicycle kicks', 'leg raises', 'sit up or crunch', 'toe taps', 'jack knife', 'mountain climber', 'scissor switch', 'Russian Twist']
		elif must_group == 'cardio':
			ex_type = ['jumping jacks', 'high knees', 'hop in place', 'jog in place', 'speed skater', ]
		chosen_excercises =[]
		for i in range(0, num_excercises): #this loop ensures no excercise is used twice
			index = randint(1, len(ex_type)) - 1
			chosen_excercises.append(ex_type[index])
			ex_type.pop(index)
		return chosen_excercises

	#assigns a time, in seconds, that each excercise should be done for.  
	def _assign_time(self, list_of_exs):
		times = []
		choose_one = range(0,90,15) #times are intervals of 15 seconds between 0 ad 90
		for i in range(0,len(list_of_exs)):
			x = randint(1, len(choose_one)) -1
			times.append(choose_one[x])
		return times

	#creates tuples of the excercise and the time it has been assigned.
	def _merge_times_and_components(self, list_of_exs, num_excercises):
		return zip(list_of_exs, num_excercises)

	#uses python's pyttsx3 library to play the workout for you.
	def _play_workout(self, zipped_t_and_c):
		list_it = list(zipped_t_and_c) #convert from a zip object to list
		for i in range(len(list_it)):
			w = 'Do ' + str(list_it[i][0]) + ' for ' + str(list_it[i][1]) + ' seconds'
			countdown = [str(i) for i in range(0, list_it[i][1], -1)]
			engine = pt.init()
			engine.say(w)
			engine.runAndWait()
			for ii in range(int(list_it[i][1])):
				print(ii)
				engine = pt.init()
				engine.say(str(ii))
				engine.runAndWait()
				time.sleep(.20)


	#Master function that calls all of the others and assembles a routine.  
	#Call this function for each muscle group you want to include.
	def build_workout(self, number, g = ['upper_body', 'lower_body', 'core', 'cardio']):
		workout = self._build_component(number, g)
		times = self._assign_time(workout)
		work_this = self._merge_times_and_components(workout, times)
		self._play_workout(work_this)

	#sample calls
	#build_workout(1, 'upper_body')
	#build_workout(3, 'lower_body')
