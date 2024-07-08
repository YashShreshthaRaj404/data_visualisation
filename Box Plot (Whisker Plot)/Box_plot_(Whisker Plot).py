import matplotlib.pyplot as plt 
eng = [82,76,24,40,67,62,78,67,72,82]
maths = [62,5,32,96,95,90,95,15,71,11]
science = [68,86,19,49,15,16,16,75,65,31]
sst = [98,10,87,29,72,16,23,72,75,30]
box_plot_data = [eng,maths,science,sst]
plt.boxplot(box_plot_data)
plt.title('Box Plot (Whisker Plot)')
plt.xticks([1,2,3,4], ["English",  "Maths", "Science", "SST"], rotation = 360)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()

