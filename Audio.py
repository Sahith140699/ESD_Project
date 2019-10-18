import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
import os
import numpy as np


def recordEditPlay2():
	fs = 44100
	sd.default.samplerate = fs
	sd.default.channels = 2

	print ("start recording...")
	duration = 10  # seconds
	myRec = sd.rec(duration * fs)
	sd.wait()

	for i in range(3, 8):
		print ("start playing...", i)
		sd.play(myRec, int(fs * i / 4))
		sd.wait()
        
recordEditPlay2()
