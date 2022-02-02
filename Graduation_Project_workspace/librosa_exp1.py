#%% 1 
import librosa 
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
#%% 2
bloom,sr = librosa.load("bloom.wav")

#%% 3 
print("*\n*\n*\n*\n*\n")
print(bloom.size)

sample_duration = 1 /sr
bloom_duration = sample_duration*len(bloom)
print(bloom_duration) 

#%% 4
plt.figure(figsize = (15,17))
librosa.display.waveplot(bloom, alpha=0.5)
plt.ylim((-1, 1))
plt.title("bloom_live_rh")

#%% 5 
FRAME_SIZE = 1024
HOP_LENGTH = 512

def amplitude_envelope(signal, frame_size, hop_length):
    """Calculate the amplitude envelope of a signal with a given frame size nad hop length."""
    amplitude_envelope = []
    
    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length): 
        amplitude_envelope_current_frame = max(signal[i:i+frame_size]) 
        amplitude_envelope.append(amplitude_envelope_current_frame)
    
    return np.array(amplitude_envelope)
#%%

ae_bloom = amplitude_envelope(bloom,1024, 512)
frames = range(len(ae_bloom))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
plt.plot(t, ae_bloom, color="r")

#%%
print(help(librosa))






















