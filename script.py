from moviepy import *


variavel = "Marvel Rivals 2025.02.19 - 15.13.05.01"


musica = VideoFileClip(variavel + ".mp4").audio
musica.write_audiofile("C:/the earrape pasta/" + variavel + ".mp3")

