# sin bank synthesizer

from impIMG import *
from scipy.signal import stft
from math import sin
from tsf import writeWav


class parameters:
	windowSize 		= 100   # Samples
	freqInterval 	= 1 	# Hz
	Fs				= 44100
	fnIN 			= "audioIN/ain.wav"
	fnOUT			= "audioOUT/aout.wav"


def loadAudio():
	p = parameters()

def getSx(fn,Mode):
    Fs,x = wavfile.read(fn)
    chnCNT = len(x.shape)
    if chnCNT == 2:
    	x = x.sum(axis=1)/2
   	# time between return values: nperseg - noverlap
   	# target = Ts
    nps = 100
    nov = 99
    f, t, Sxx = signal.spectrogram(x,Fs,nperseg = nps,noverlap=nov,mode=Mode)
    return(f,t,Sxx)

def oscSynth(freqIdx,timeIdx,mag,ph):
	
	synthOut = np.zeros(1)
	for i in range(len(timeIdx)):
		sample = 0
		for j in range(len(freqIdx)):
			sample += mag[j,i]*sin(freqIdx[j]*timeIdx[i]+ph[j,i])
		synthOut = np.append(synthOut,sample)			

	synthOut = synthOut[1:]
	return(synthOut)

def main():
	print('yo!')
	p = parameters()

	# load audio file into spectrogram
	f,t,mag = getSx(p.fnIN,'magnitude')
	f,t,phase = getSx(p.fnIN,'phase')


	# iterate through freqency steps
		# compute magnitude phase component for osc
		# sum

	# write synthesized audio

if __name__ == "__main__":
	# main()
	print('yo!')
	p = parameters()

	# load audio file into spectrogram
	f,t,mag = getSx(p.fnIN,'magnitude')
	f,t,phase = getSx(p.fnIN,'phase')
	synthOut = oscSynth(f,t,mag,phase)

	writeWav(synthOut,p.Fs,p.fnOUT)
	writeWav(synthOut,p.Fs,p.fnOUT+time.strftime("%Y%m%d-%H%M%S"))


