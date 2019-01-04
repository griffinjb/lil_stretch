# sin bank synthesizer

from impIMG import *
from scipy.signal import stft
from math import sin
from tsf import writeWav
from samplerate import resample

class parameters:
	windowSize 		= 100   # Samples
	freqInterval 	= 1 	# Hz
	Fs				= 44100
	stretchFactor	= 2
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

def linStretch(a1d,l):
	print('yo!')
	p = parameters()
	out = np.zeros(l)
	out[0] = a1d[0]
	for i in range(l-1):
		out[i+1] = out[i]+(a1d[1]-a1d[0])/p.stretchFactor

	return(out)



def stretch(a2d):
	p = parameters()

	try:
		newSize = int(len(resample(a2d[0,:],p.stretchFactor,'sinc_best')))

		out = np.zeros([a2d.shape[0],newSize])

		for i in range(a2d.shape[0]):
			# out[i,:] = resample(a2d[i,:],newSize)
			out[i,:] = resample(a2d[i,:],p.stretchFactor,'sinc_best')

	except:
		newSize = int(len(resample(a2d[:],p.stretchFactor,'sinc_best')))

		out = np.zeros([1,newSize])

		for i in range(a2d.shape[0]):
			# out[i,:] = resample(a2d[i,:],newSize)
			out = resample(a2d[:],p.stretchFactor,'sinc_best')


	return(out)


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

	print('computing spectrogram...')

	# load audio file into spectrogram
	f,t,mag = getSx(p.fnIN,'magnitude')
	f,t,phase = getSx(p.fnIN,'phase')

	print('stretching magnitude')
	magS = stretch(mag)
	print('stretching phase')
	phaseS = stretch(phase)
	print('stretching time idx')
	tS = linStretch(t,phaseS.shape[1])


	print('Synthesizing audio')
	synthOut = oscSynth(f,tS,magS,phaseS)

	print('Writing wav')
	writeWav(synthOut,p.Fs,p.fnOUT)
	writeWav(synthOut,p.Fs,p.fnOUT+time.strftime("%Y%m%d-%H%M%S"))


