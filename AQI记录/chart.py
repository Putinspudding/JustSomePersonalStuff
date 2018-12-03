import matplotlib.pyplot as plt
import datetime

time = []
aqi = []
filename = str(datetime.date.today())
file = open("AQI/AQI"+filename+".txt", "r+")
line = file.readline()
while line:
    time.append(int(line[0:2]))
    aqi.append(int(line[3:6]))
    line = file.readline()
file.close()
plt.bar(time, aqi, width=0.25)
plt.xticks(time)
plt.xlim()
plt.ylim(0, 300)
for x, y in zip(time, aqi):
    plt.text(x, y, '%d' % y, ha='center', va='bottom')
plt.savefig("AQI/AQI"+filename)
