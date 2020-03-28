import numpy as np
#import pyttsx3 as pt
from random import randint
import os
import time
import abc
from src.excercises import groups
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from src.credentials import creds
from pydub import AudioSegment
from pydub.playback import play
import wave


AUTHENTICATOR = IAMAuthenticator('{}'.format(creds['apikey']))
TEXT_TO_SPEECH = TextToSpeechV1(
    authenticator=AUTHENTICATOR
)
TEXT_TO_SPEECH.set_service_url('{}'.format(creds['url']))

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
		choose_one = range(15,90,15) #times are intervals of 15 seconds between 15 and 90 -- dont want to choose 0!
		for i in range(0,len(list_of_exs)):
			x = randint(1, len(choose_one)) -1
			times.append(choose_one[x])
		return times

	#creates tuples of the excercise and the time it has been assigned.
	def _merge_times_and_components(self, list_of_exs, num_excercises):
		return zip(list_of_exs, num_excercises)


	def _get_sound_files(self, zipped_t_and_c):
		sound_files =[]
		for ex, count in list(zipped_t_and_c):
			f_name = ('audio/'+ str(ex)+ '_' + str(count) + '.wav').replace(' ','_')
			sound_files.append((f_name, count))
			with open(f_name, 'wb') as audio_file:
				#DONT SAVE IT AS A VARIABLE -- the sound file is created, and that is what we want and will play in the next step.
				try:
					audio_file.write(TEXT_TO_SPEECH.synthesize(str(ex), voice='en-US_AllisonVoice', accept='audio/wav').get_result().content)
				except Exception as error:
					print("Exception retrieving voice file: {}".format(error))
			audio_file.close()
		return sound_files

	#def _play_workout(self):				
	def _play_workout(self, workout, times, sound_files):
		#just parse the string -- its in there.  way easier.
		for i in range(0, len(sound_files)):
			f_path = os.path.abspath(sound_files[i][0])
			print(f_path)
			print(sound_files[i][1])
			sound = AudioSegment.from_wav(f_path)
			play(sound)
			print("sleeping for " + str(sound_files[i][1]) + " seconds")
			time.sleep(sound_files[i][1])

	#Master function that calls all of the others and assembles a routine.  
	#Call this function for each muscle group you want to include.
	def build_workout(self, number, g):
		g = self._sanitize_inputs(g)
		workout = self._build_component(number, g)
		times = self._assign_time(workout)
		record_this = self._merge_times_and_components(workout, times)
		print("working out go away")
		#self._play_workout(work_this)
		sound_files = self._get_sound_files(record_this)
		self._play_workout(workout, times, sound_files) #we have dumped the ap

		#move this to the beginning-- then no risk of deleting files we need still
		os.getcwd()
		os.remove("/audio")


#Workout().build_workout(2, 'upper_body')
