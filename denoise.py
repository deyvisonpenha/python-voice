get_ipython().system('pip install noisereduce')

import librosa
import noisereduce as nr
import numpy as np
from IPython.display import Audio
import math


path = '/Users/airpenha/Projects/python/pmo/131139Z.mp3'
data, fs = librosa.load(path)



time = np.arange(0, len(data))/fs
n = len(time)
total_time_seconds = len(data)/fs


time_end = math.floor(time[n-1])
noisy_part = data[0:3627534]
# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)

Audio(data=reduced_noise,rate=fs)
Audio(data=data,rate=fs)


snr = 20 # signal to noise ratio = 20
noise_clip = data/snr
audio_clip_filtred = reduced_noise + noise_clip


Audio(data=audio_clip_cafe,rate=fs)



noise_reduced = nr.reduce_noise(audio_clip=reduced_noise.astype('float32'),
                                noise_clip=noise_clip.astype('float32'),
                                use_tensorflow=True, 
                                verbose=False)

Audio(data=noise_reduced,rate=fs)

