import matplotlib.pyplot as plt
import numpy as np
import serial
import time

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)

line1 = s.readline()
line2 = s.readline()
time2 = float(line2)

print(line2)
print(time2)


Fs = 200.0/time2*1000000  # sampling rate
Ts = 1.0/Fs # sampling interval
t = np.arange(0,time2/1000000,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
y = np.arange(0,time2/1000000,Ts) # signal vector; create Fs samples

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # a vector of frequencies; two sides frequency range
#print(n)
#print(T)
frq = frq[range(6)] # one side frequency range


for x in range(0, int(n)):
    line=s.readline() # Read an echo string from B_L4S5I_IOT01A terminated with '\n'
    # print line
    y[x] = float(line)

    

Y = np.fft.fft(y)/n*2 # fft computing and normalization
Y = Y[range(6)] # remove the conjugate frequency parts

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.show()
s.close()