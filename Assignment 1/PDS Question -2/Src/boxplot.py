import matplotlib.pyplot as plt
import pandas as pandas
import seaborn as seaborn
Students_Performance_data = pandas.read_csv("StudentsPerformance.csv")
seaborn.boxplot(x="gender",y="math score",data=Students_Performance_data)
plt.title("Gender based math scores")	
plt.show()
