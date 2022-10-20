import sounddevice
from scipy.io.wavfile import write

fs = 44100

# The record duration of your choice
seconds = 120
print("Recording in progress... ")
my_recording = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)

# This makes it wait until the recording is finished.

sounddevice.wait()
write('output.wav', fs, my_recording)
print("Your recording has been saved ✌")
