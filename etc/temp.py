import matplotlib.pyplot as plt

x = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
y1 = ["15.6","14.2","16.3","18.2","17.1","20.2","22.4"]
y2 = ["20.1","23.1","23.8","25.9","23.4","25.1","26.3"]

plt.plot(x,y1,label='seoul')
plt.plot(x,y2,label='busan')
plt.xlabel('day')
plt.ylabel('temp')
plt.legend(loc='upper left')
plt.title('Temp of Cities')
plt.show()