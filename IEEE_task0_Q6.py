import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
#Importing the required libraries

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "final_student_performance.csv"
df = pd.read_csv(csv_path)
#Importing the .csv file

plt.figure(figsize=(20, 20))
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Students")
plt.ylabel("Final Score")
plt.title("Students' Final Scores")
plt.yticks(np.arange(0, 100, 5))
plt.xticks(rotation=90)
plt.show()
#Creating the bar graph to show Student v/s Final Scores

plt.figure(figsize=(20, 20))
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Final Scores")
plt.yticks(np.arange(0, 100, 5))
plt.xticks(np.arange(0, 10, 0.5))
plt.title("Hours Studied v/s Final Score")
plt.show()
#Creating the scatter graph to show Hours Studied v/s Final Scores

plt.figure(figsize=(20, 20))
plt.hist(df["Final_Score"], edgecolor="black")
plt.xlabel("Final Scores")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 30, 2))
plt.title("Histogram of the Final Scores")
plt.show()
#Creating the histogram to show the frequency of each score

plt.figure(figsize=(20, 20))
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Scores")
plt.yticks(np.arange(0, 100, 5))
plt.xticks(np.arange(0, 100, 5))
plt.title("Attendance v/s Final Score")
plt.show()
#Creating a scatter graph to show Attendance v/s Final Score
