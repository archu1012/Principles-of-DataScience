import matplotlib.pyplot as plt
import pandas as pandas
import seaborn as seaborn
Students_Performance_data = pandas.read_csv("StudentsPerformance.csv")
corr=Students_Performance_data.corr(numeric_only=True)
colormap = seaborn.color_palette("Greens")
seaborn.heatmap(corr,cmap=colormap,annot=True)
plt.title("Correlation Matrix")
plt.show()
