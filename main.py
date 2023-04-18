import gtts
from playsound import playsound
f = open("cider.txt").read()
t1 = gtts.gTTS(f)
t1.save("уу.mp3")