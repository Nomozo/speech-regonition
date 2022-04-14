
from speech_recognition import Microphone,Recognizer,AudioFile
import pyaudio
recog = Recognizer()
mic= Microphone()

with mic:
    print("talk")
    audio =recog.record(mic,3)
    
    recognized = recog.recognize_google(audio)
    print("you said:",recognized)