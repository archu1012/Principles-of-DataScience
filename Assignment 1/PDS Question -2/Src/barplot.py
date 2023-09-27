import matplotlib.pyplot as plt
import pandas as pandas
Students_Performance_data = pandas.read_csv("StudentsPerformance.csv")
gender_frequency = Students_Performance_data['gender'].value_counts()
plt.title("Gender Separation")
plt.xlabel("Gender")
plt.ylabel("count")
plt.bar(gender_counts.index,gender_frequency.values,color="yellow")
