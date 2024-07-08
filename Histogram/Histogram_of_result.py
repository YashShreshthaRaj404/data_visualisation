from matplotlib import pyplot as plt 
import numpy as np 
fig,ax = plt.subplots(1,1)
marks = np.array([19,16,28,45,37,34,13,49,42,44])
ax.hist(marks, bins = [10,20,30,40,50])
ax.set_title("Histogram Of Results")
ax.set_xlabel('Marks')
ax.set_ylabel('No. of Students')
plt.show()