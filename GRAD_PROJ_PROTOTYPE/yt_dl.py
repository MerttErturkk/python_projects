import youtube_dl
import os
#%%
options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3 
  'outtmpl': '%(id)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}
  # save file as the YouTube ID
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=NKwJYZlD3IM"])
    
#%%
os.rename("NKwJYZlD3IM","NKwJYZlD3IM.wav")


options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3 
  'outtmpl': '%(id)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

#%%
from pydub import AudioSegment
t1 = 10 * 1000 #Works in milliseconds
t2 = 20 * 1000
newAudio = AudioSegment.from_file(r"NKwJYZlD3IM.mp3")
newAudio = newAudio[t1:t2]
newAudio.export('newSong.wav', format="wav") #Exports to a wav file in the current path.

#%%
import pandas as pd
df= pd.read_csv(r"features_3_sec.csv")

for c in df.columns:
    print(c)
print("\n\n\n")
print(df.label.unique())


print("\n\n\n")
print(df.tempo.sort_values().unique())