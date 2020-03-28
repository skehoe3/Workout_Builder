from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from credentials import creds

#docs: https://cloud.ibm.com/apidocs/text-to-speech/text-to-speech?code=python

from src.workout import Workout

# authenticator = IAMAuthenticator('{}'.format(creds['apikey']))
# text_to_speech = TextToSpeechV1(
#     authenticator=authenticator
# )

# text_to_speech.set_service_url('{}'.format(creds['url']))
# #text_to_speech.set_disable_ssl_verification(True)
# with open('hello_world.wav', 'wb') as audio_file:
#     audio_file.write(
#         text_to_speech.synthesize(
#             'Hello world',
#             voice='en-US_AllisonVoice',
#             accept='audio/wav'        
#         ).get_result().content)

