#import os
#os.getcwd()  # returns the working directory
# os.chdir(path) # change the working directory
#os.rename("king of limbs","king of limbs.wav")
# %timeit for x in range(100): function(x)


#%%
def song_download(web_link,destination,sample_name,t_sec):
    """
    Download and store 10 second audio sample from YOUTUBE link.

    Parameters
    ----------
    web_link : string
        The youtube link that we get the audio sample from.
    destination : string
        The destination which we will store the sample .wav file
    sample_name : string
        Name of the sample for future references.
    t_sec : TYPE, INT
        Timestamp in seconds which the 10 second sample begins.

    Returns
    -------
    True

    """
    import youtube_dl
    from pydub import AudioSegment
    import os
    
    options = {
      'format': 'bestaudio/best',
      'extractaudio' : True,  # only keep the audio
      'audioformat' : "wav",  # convert to wav
      'outtmpl': 'temp.wav',    # '%(id)s' == name the file the ID of the video
      'noplaylist' : True,    # only download single song, not playlist
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([web_link])
    # THIS STEP TAKES SOME TIME
    
    t1 = t_sec * 1000 #Works in milliseconds
    t2 = (t_sec +10)* 1000
    AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
    newAudio = AudioSegment.from_file(r'C:\Users\mertt\temp.wav')
    newAudio = newAudio[t1:t2]
    
    newAudio.export(destination +"\\" + sample_name + ".wav", format="wav") #Exports to a wav file in the current path.
    os.remove(r'C:\Users\mertt\temp.wav')
    print("Downloaded:"+destination+"\\" +sample_name +".wav")
    
    return True

#%%
web_link = "https://www.youtube.com/watch?v=hTWKbfoikeg"
destination = r'C:\Users\mertt\OneDrive\Desktop\GRAD\ROCK'
sample_name = "teen_spirit"
t_sec = 10


song_download(web_link, destination, sample_name, t_sec)


#%% 1 
import librosa 
import librosa.display
import matplotlib.pyplot as plt
#%% 2
acid,sr = librosa.load(r"C:\Users\mertt\OneDrive\Desktop\GRAD\sample.mp3")

#%% 3 
print("*\n*\n*\n*\n*\n")
print(acid.size)

sample_duration = 1 /sr
acid_duration = sample_duration*len(acid)
print(acid_duration) 

#%% 4
plt.figure(figsize = (15,17))
librosa.display.waveplot(acid, alpha=0.5)
plt.ylim((-1, 1))
plt.title("acidrain_time_domain")

#%% 5 
def abc(series):
    5 
import pandas as pd
import numpy as np
rectified_audio = pd.Series(acid).apply(np.abs)
energy_envelope = rectified_audio.rolling(window = 50).mean().dropna()

plt.figure(figsize = (15,17))
plt.plot(energy_envelope.index/22050 , energy_envelope, alpha=0.5)
plt.ylim((0, 1))
plt.title("acidrain_energy_envelope")


#%%
from scipy import signal
plt.figure(figsize = (15,17))
f, t, Sxx = signal.spectrogram(acid, sr,nperseg=1024,noverlap = 256)
plt.ylim(top=1000)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
