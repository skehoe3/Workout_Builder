import numpy as np
import pyttsx3 as pt
from random import randint
import time
import abc
from src.excercises import groups

class Workout():
	# TODO:
	#randomly selects the number of excercises specified from the muscle group desired.
	#reformat user input to match the options in the app
	def _sanitize_inputs(self, musc_group):
		return musc_group.strip().replace(' ', '_')

	def _build_component(self, num_excercises, musc_group = ['upper_body', 'lower_body', 'core', 'cardio']):
		
		chosen_excercises =[]
		for i in range(0, num_excercises): #this loop ensures no excercise is used twice
			index = randint(0, len(groups[musc_group])) - 1
			chosen_excercises.append(groups[musc_group][index])
			groups[musc_group].pop(index)
		return chosen_excercises

	#assigns a time, in seconds, that each excercise should be done for.  
	def _assign_time(self, list_of_exs):
		times = []
		choose_one = range(0,90,15) #times are intervals of 15 seconds between 0 and 90
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
				#print(ii)
				engine = pt.init()
				engine.say(str(ii))
				engine.runAndWait()
				time.sleep(.20)


	#Master function that calls all of the others and assembles a routine.  
	#Call this function for each muscle group you want to include.
	def build_workout(self, number, g):
		g = self._sanitize_inputs(g)
		workout = self._build_component(number, g)
		times = self._assign_time(workout)
		work_this = self._merge_times_and_components(workout, times)
		print("working out go away")
		self._play_workout(work_this)