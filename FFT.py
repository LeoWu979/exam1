import matplotlib.pyplot as plt
import numpy as np
import serial
import time

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)

#line1 = s.readline()
#line2 = s.readline()
#time2 = float(line2)

#print(line2)
#print(time2)


Fs = 120.0/240*1000  # sampling rate
Ts = 1.0/Fs # sampling interval
t1 = np.hstack([np.arange(0,10/1000,0.25/1000) , np.arange(10/1000,230/1000,5.5/1000), np.arange(230/1000,240/1000,0.25/1000)])
t2 = np.hstack([np.arange(0,20/1000,0.5/1000) , np.arange(20/1000,220/1000,5/1000), np.arange(220/1000,240/1000,0.5/1000)])
t3 = np.hstack([np.arange(0,40/1000,1/1000) , np.arange(40/1000,200/1000,4/1000), np.arange(200/1000,240/1000,1/1000)])
t4 = np.hstack([np.arange(0,80/1000,2/1000) , np.arange(80/1000,160/1000,2/1000), np.arange(160/1000,240/1000,2/1000)])


#y = np.hstack([np.arange(0,10/1000,0.25/1000) , np.arange(10/1000,230/1000,5.5/1000), np.arange(230/1000,240/1000,0.25/1000)])

y1 = np.hstack([np.arange(0,10/1000,0.25/1000) , np.arange(10/1000,230/1000,5.5/1000), np.arange(230/1000,240/1000,0.25/1000)])
y2 = np.hstack([np.arange(0,20/1000,0.5/1000) , np.arange(20/1000,220/1000,5/1000), np.arange(220/1000,240/1000,0.5/1000)])
y3 = np.hstack([np.arange(0,40/1000,1/1000) , np.arange(40/1000,200/1000,4/1000), np.arange(200/1000,240/1000,1/1000)])
y4 = np.hstack([np.arange(0,80/1000,2/1000) , np.arange(80/1000,160/1000,2/1000), np.arange(160/1000,240/1000,2/1000)])
#y = np.arange(0,480/1000,Ts) # signal vector; create Fs samples

print(t)

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