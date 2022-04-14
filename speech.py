import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Okam gapiring...")
    
    audio_text = r.listen(source)
    print("o'ylayapman")
try:
    print('text:'+r.recognize_google(audio_text))  
except:
    print("Topolmadim")