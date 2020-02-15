"""
:author: Marcus Tran
:date: February 15, 2020
:description: Program under the GUI and Frontend of the program, displays an image of a
spectrogram for a file that has been inputted into the front end
:specifications: Does not communicate or involve the backend, only helps display an image to provide better
interaction with the GUI and user
"""

from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

class Spectrogram:

    def main(self, AudioFile):
        AudioName = AudioFile
        try:
            (AudioName.endswith('.wav'))
            fs, Audiodata = wavfile.read(AudioName)

        except Exception as error:
            print("Wrong file type inputted, please try another: ", AudioFile)
            return None

        plt.plot(Audiodata)
        plt.title('Audio Signal in Time', size=16)

        from scipy.fftpack import fft
        n = len(Audiodata)
        AudioFreq = fft(Audiodata)
        AudioFreq = AudioFreq[0:int(np.ceil((n+1)/2.0))]
        MagFreq = np.abs(AudioFreq)
        MagFreq = MagFreq / float(n)

        MagFreq = MagFreq**2

        if n % 2 > 0:
            MagFreq[1:len(MagFreq)] = MagFreq[1:len(MagFreq)] * 2
        else:
            MagFreq[1:len(MagFreq) -1] = MagFreq[1:len(MagFreq) - 1] * 2

        plt.figure()
        freqAxis = np.arrange(0,int(np.ceil((n+1)/2.0), 1.0) * (fs / n))
        plt.plot(freqAxis/1000.0, 10*np.log10(MagFreq))
        plt.xlabel('Frequency (kHz)')
        plt.ylabel('Power spectrum (dB)')

        from scipy import signal
        N = 512
        f, t, Sxx = signal.spectrogram(Audiodata, fs, window=signal.blackman(N), nfft=N)