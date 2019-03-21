import numpy as np
from matplotlib import pyplot as plt
import requests
from datetime import datetime as dt
import time as sleep_time

t = np.zeros(100)
y = np.zeros(100)
time = 0

plt.ion()
plt.figure()
li, = plt.plot(t, y)
plt.ylim(0, 7000)
plt.xlabel("time")
plt.ylabel("Power[*10^8 W]")

url = 'http://tepco-usage-api.appspot.com/quick.txt'

while True:
    try:
        response = requests.get(url)

        time += 1
        demand = int(response.text.split(",")[1])
        supply = int(response.text.split(",")[2])

        t = np.append(t, time)
        t = np.delete(t, 0)
        y = np.append(y, demand)
        y = np.delete(y, 0)
        
        li.set_xdata(t)
        li.set_ydata(y)           
        plt.xlim(min(t), max(t))
        plt.draw()
        plt.pause(300)

    except KeyboardInterrupt:
        break