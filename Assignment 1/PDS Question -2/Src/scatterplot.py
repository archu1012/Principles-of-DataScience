import matplotlib.pyplot as plt
import pandas as pandas
import seaborn as seaborn
Students_Performance_data = pandas.read_csv("StudentsPerformance.csv")
plt.scatter(Students_Performance_data['math score'],Students_Performance_data['reading score'],color='red')
plt.title("Mathematics scores vs Reading scores")
plt.xlabel("Math Score from dataset")
plt.ylabel("reading score from dataset")
plt.show()
