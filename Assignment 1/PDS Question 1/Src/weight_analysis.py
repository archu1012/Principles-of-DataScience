import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\clean_data\\processed_data.csv')
plt.ylabel("Weight")
plt.title("Weight Analysis")
plt.boxplot(df.Weight)
plt.savefig('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\results\\weight_distribution.png')
