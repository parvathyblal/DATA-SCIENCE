LINE WITH GRID

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
x=(["mon","tue","wed","thur","fri","sat"])
y=([10,20,30,40,50,60])
plt.plot(x,y)
plt.plot(x,y,ls="-.",color="r",marker="*",markerfacecolor="g",markersize=20)
plt.title("sales data1")
plt.xlabel("day of week")
plt.ylabel("sales of drink")
plt.grid()
plt.subplot(1,2,2)
x=(["mon","tue","wed","thur","fri","sat"])
y=([10,20,30,40,50,60])
plt.plot(x,y)
plt.plot(x,y,ls="-.",color="r",marker="*",markerfacecolor="g",markersize=20)
plt.title("sales data2")
plt.xlabel("day of week")
plt.ylabel("sales of food")
plt.grid()
plt.show()
