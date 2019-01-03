# sin bank synthesizer

from impIMG import *
from scipy.signal import stft



class parameters:
	windowSize 		= 100   # Samples
	freqInterval 	= 1 	# Hz
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

def main():
	print('yo!')
	p = parameters()

	# load audio file into spectrogram
	f,t,mag = getSx(p.fnIN,'magnitude')	
	f,t,phase = getSx(p.fnIN,'phase')



	# compute stft

	# iterate through freqency steps
		# compute magnitude phase component for osc
		# sum

	# write synthesized audio




if __name__ == "__main__":
	main()

