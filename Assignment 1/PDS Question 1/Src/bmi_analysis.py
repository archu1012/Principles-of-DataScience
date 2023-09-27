import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\clean_data\\processed_data.csv')
colors = []
for value in df.BMI: 
    if value <= 18.5:
        colors.append('gray')
    elif value > 18.5 and value <= 25:
        colors.append('green')
    elif value > 25 and val <=30:
        colors.append('orange')
    else:
        colors.append('red')
fig = plt.figure()
ax = fig.add_subplot(111)
width = 0.5
custom_lines = [Line2D([0], [0], color='gray', lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='orange', lw=4),
                Line2D([0], [0], color='red', lw=4)]
ax.legend(custom_lines, ['Under Weight', 'Correct Weight', 'Over Weight', 'Obese'])
ax.bar(df.Person, df.BMI, width, color=colors)
plt.xticks(np.arange(0, 10, 1.0))
plt.ylim(0, 30)
plt.xlabel("Person")
plt.ylabel("BMI")
plt.title("BMI Analysis")
plt.savefig('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\results\\bmi_analysis.png')
plt.show()
