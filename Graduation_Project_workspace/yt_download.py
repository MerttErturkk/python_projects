import youtube_dl
import os
# os.getcwd()  # returns the working directory
# os.chdir(path) # change the working directory

# %timeit for x in range(100): function(x)
#%%

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "wav",  # convert to wav
  'outtmpl': 'king of limbs',    # '%(id)s' == name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=hI5YMDioDBY&t=1667s"])
    
os.rename("king of limbs","king of limbs.wav")

#%%
from pydub import AudioSegment

t1 = 215 * 1000 #Works in milliseconds
t2 = 396 * 1000
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
newAudio = AudioSegment.from_file(r"C:\Users\mertt\OneDrive\Desktop\GRAD\king of limbs.wav")
newAudio = newAudio[t1:t2]

newAudio.export(r"C:\Users\mertt\OneDrive\Desktop\GRAD\bloom.mp3", format="mp3") #Exports to a wav file in the current path.
