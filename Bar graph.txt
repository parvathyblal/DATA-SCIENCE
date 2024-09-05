import matplotlib.pyplot as plt
import numpy as np
x= np.array(['walking','cycle','car','bus','train'])
y = np.array([10,4,5,1,3])
plt.bar(x,y,color='maroon')
plt.title('Transportation Details')
plt.xlabel('mode of transport')
plt.ylabel('no. of students')
plt.show()
