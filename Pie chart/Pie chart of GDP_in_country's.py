"""
    here's are a Pie Chart of some Country's 
GDP in $US Trillions......
"""
from matplotlib import pyplot as plt 
import numpy as np 
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
country = ["India","USA","Japan","Russia","Italy","Brazil","Australia","Mexico"]
GDP = [3.41,25.43,4.231,2.24,2.04,1.920,1.69,1.46]
ax.pie(GDP, labels = country, autopct = '%1.2f%%')
print("Pie Chart of some Country's \nGDP in $Trillions")
plt.show()