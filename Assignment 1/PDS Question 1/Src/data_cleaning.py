import pandas as pd
df = pd.read_csv('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\raw_data\\given_raw_data.csv')
df = df.rename(columns={"Height (Inches)": "Height", "Weight (Pounds)": "Weight"})
df.to_csv('C:\\Users\\Archana\\OneDrive\\Documents\\PDS\\Assignments\\clean_data\\cleaned_data.csv')

