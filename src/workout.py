
import os
import time
from random import randint

import numpy as np
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from pydub import AudioSegment
from pydub.playback import play

# in credentials, save your API credentials for IBM's text to speech
from src.credentials import creds
from src.excercises import groups

# Import credentials
AUTHENTICATOR = IAMAuthenticator("{}".format(creds["apikey"]))
TEXT_TO_SPEECH = TextToSpeechV1(authenticator=AUTHENTICATOR)
TEXT_TO_SPEECH.set_service_url("{}".format(creds["url"]))


class Workout():
    def _sanitize_inputs(self, musc_group):
        """
                takes in the muscle group listed and converst spaces to underscores.
                Args:
                        musc_group (string): desired group

                Returns:
                        string: whitespace replaced with underscores
                """
        return musc_group.strip().replace(" ", "_")

    def _build_component(self, num_excercises, musc_group):
        """
                randomly chooses the prescribed number of excercises for the prescribed
                muscle group
                Args:
                        num_excercises (integer): number of moves to do
                        musc_group (string): section of the body to train

                Returns:
                        list: list of the excercises to do
                """

        chosen_excercises = []
        # this loop ensures no excercise is used twice
        for i in range(0, num_excercises):
            index = randint(0, len(groups[musc_group])) - 1
            chosen_excercises.append(groups[musc_group][index])
            groups[musc_group].pop(index)
        return chosen_excercises

    def _assign_time(self, list_of_exs):
        """
                assigns a time, in seconds, that each excercise should be done for.
                Args:
                        list_of_exs (list): the excercises to be performed

                Returns:
                        list: list of the amount of time, in seconds, each excercise should
                        be done for
                """
        times = []
        # times are intervals of 15 seconds between 15 and 90
        # -- dont want to choose 0!
        choose_one = range(15, 90, 15)
        for i in range(0, len(list_of_exs)):
            x = randint(1, len(choose_one)) - 1
            times.append(choose_one[x])
        return times

    def _merge_times_and_components(self, list_of_exs, times):
        """
                creates tuples of the excercise and the time it has been assigned.
                Args:
                        list_of_exs (list):  excercises to be performed
                        times (list): times for each excercise to be done

                Returns:
                        [zip object]: zip of the excercises and duration
                """
        return zip(list_of_exs, times)

    def _get_sound_files(self, zipped_t_and_c):
        """
                Posts the spoken workout to the IBM text to speech endpoint.  
                Args:
                        zipped_t_and_c (zip object): the pairing of the excercise and how
                                long it should be done for

                Returns:
                        list: list of tuples with the WAV file name and duration of the 
                                excercise
                """
        sound_files = []
        for ex, count in list(zipped_t_and_c):
            f_name = ("audio/" + str(ex) + "_" +
                      str(count) + ".wav").replace(" ", "_")
            sound_files.append((f_name, count))
            with open(f_name, "wb") as audio_file:
                # DONT SAVE IT AS A VARIABLE -- the sound file is created, and that is what we want and will play in the next step.
                try:
                    audio_file.write(
                        TEXT_TO_SPEECH.synthesize(
                            "Do " + str(ex) + " for " +
                            str(count) + " seconds",
                            voice="en-US_AllisonVoice",
                            accept="audio/wav",
                        )
                        .get_result()
                        .content
                    )
                except Exception as error:
                    print("Exception retrieving voice file: {}".format(error))
            audio_file.close()
        return sound_files

    def _play_workout(self, sound_files):
        """
                Plays the workout aloud.
                Args:
                        sound_files (list of tuples): (wav file name, duration of excercise)
                """
        for i in range(0, len(sound_files)):
            f_path = os.path.abspath(sound_files[i][0])
            sound = AudioSegment.from_wav(f_path)
            play(sound)
            print("sleeping for " + str(sound_files[i][1]) + " seconds")
            time.sleep(sound_files[i][1])

    def build_workout(self, number, g):
        """
                Master function that calls all of the others and assembles a routine.
        Call this function for each muscle group you want to include.
                Args:
                        number (int): [number of excercises to do]
                        g (string): muscle group to target
                """
        g = self._sanitize_inputs(g)
        workout = self._build_component(number, g)
        times = self._assign_time(workout)
        record_this = self._merge_times_and_components(workout, times)
        sound_files = self._get_sound_files(record_this)
        self._play_workout(sound_files)
        # remove files now that we are done with them
        for f in os.listdir("audio/"):
            if ".DS_Store" in "audio/" + str(f):
                pass
            os.remove(str("audio/" + f))
