import pandas as pd
#importing pandas

df = pd.read_csv("student_performance.csv")
#1. Load the CSV into a DataFrame.

print("\n", df[:5])
#2. Print the first five rows.

print(f"\n(Rows, Columns) of the DataFrame: {df.shape}")
#3. Print the number of rows and columns.

print(f"\nColumn names: {df.columns.tolist()}")
#4. Display the column names.

print("\nChecking for missing values in the DataSet:")
print(pd.isna(df).all())
#5. Check whether the dataset contains missing values.

print(f"\nThe average Final Score is: {df["Final_Score"].mean()}")
#6. Calculate the average Final_Score.

highest_score = df["Final_Score"].max()
top_students = df[df["Final_Score"] == highest_score]
print("\nHighest score:", highest_score)
print("Student:", top_students["Student"])
#7. Find the student with the highest Final_Score

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
#8. Create a new column: Improvement = Final_Score - Previous_Score.

greater_attendace = df[df["Attendance"] >= 80]
print("\nStudents with attendance greater than or equal to 80:\n", greater_attendace["Student"])
#9. Display only students with attendance greater than or equal to 80.

df = df.sort_values(by="Final_Score", ascending=False)
#10. Sort the DataFrame by Final_Score in descending order.

df.to_csv('final_student_performance.csv', index=False)
#11. Save the processed DataFrame as processed_student_performance.csv