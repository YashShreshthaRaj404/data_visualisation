"""
    since, Scatter Plot Of John's Semester wise marks...
therefore, total marks is 50  
"""
import matplotlib.pyplot as plt
semesterI_marks = [31,38,42,40,49,50,39]
semesterII_marks = [36.6,38.1,44,21,41,15,45]
plt.scatter( semesterI_marks,semesterII_marks, c='black')
plt.title("The Scatter Plot Of John's Semester Marks Is")
plt.xlabel ( 'I-Semester marks')
plt.ylabel ( 'II-Semester marks')
plt.show ()