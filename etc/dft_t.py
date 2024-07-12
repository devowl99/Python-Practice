from matplotlib import pyplot as plt
import numpy as np
            
T1=0
T2=1
fs=64
ts=1/fs
pi=3.14
j=(-1)**(0.5)

t_vec=np.arange(T1,T2,ts)
N=len(t_vec)
x=10*np.cos(2*pi*10*t_vec)+np.cos(2*pi*5*t_vec)
fre_vec=np.arange(0, 2*pi, 2*pi/N)

X=[]
for k in range(len(fre_vec)):
    x_kn=0
    for n in range(len(t_vec)):
        x_kn+=x[n]*np.exp(-1*j*2*np.pi/N*k*n)
        #x_kn+=x[n]*np.cos(2*np.pi/N*k*n)
    X.append(abs(x_kn))
X=np.array(X)*(2/len(X))   

X_i=[]
for n in range(len(t_vec)):
    x_kn_i=0
    for k in range(len(fre_vec)):
        x_kn_i+=X[k]*np.exp(1*j*2*np.pi/N*k*n)
    X_i.append(x_kn_i/N)
X_i=np.array(X_i)/(2/len(X))     

fft_r=np.fft.fft(x)
abs_f=abs(fft_r)*(2/len(fft_r))
fre=np.fft.fftfreq(len(fft_r),ts)
fre_v=np.fft.fftfreq(len(X),ts)

plt.figure(1)    
plt.plot(t_vec, x, 'r')
plt.xlabel('time')
plt.ylabel('x[n]')
plt.grid()
plt.figure(2)    
plt.xlim(-30,30)
plt.stem(fre_v,X)
plt.xlabel('F')
plt.ylabel('|X[k]|')
plt.grid()
plt.figure(3)    
plt.plot(t_vec, X_i, 'r')
plt.xlabel('time')
plt.ylabel('x[n]')
plt.grid()
plt.figure(4)    
plt.xlim(-30,30)
plt.stem(fre, abs_f)
plt.xlabel('F')
plt.ylabel('|X[k]|')
plt.grid()
plt.show()


