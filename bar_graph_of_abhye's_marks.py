'''
this is a marks of Abhye's.....
To show marks from BAR CHART..

'''
import matplotlib.pyplot as plt
No_of_marks_obtained = [35,32,39,37,28,40,32,16.5]
plt.bar(['Hindi','English','Math','Science','SST','AI','Sanskrit','Psychology'],No_of_marks_obtained)
plt.title('Bar Chart Of Abhye Marks')
plt.xlabel('Subjects')
plt.ylabel('No. of marks obtained')
plt.show()