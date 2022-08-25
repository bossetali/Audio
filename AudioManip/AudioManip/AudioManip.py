
import matplotlib.pyplot as plt


file = open("spectrum.txt","r+")

lines=files.readlines()

x = [line.split()[0] for line in lines]
y = [line.split()[1] for line in lines]

fig=plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title")    
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')

ax1.plot(x,y, c='r', label='the data')

leg = ax1.legend()

plt.show()

file.close()
