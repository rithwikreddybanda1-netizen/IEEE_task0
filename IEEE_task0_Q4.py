#importing numpy library
import numpy as np

#creating numpy arrays and giving them random values
hours = np.array([2.5, 5.2, 8.1, 3.6, 6.7])
attendance = np.array([100, 76, 91, 83, 77])
prev_scores = np.array([54, 86, 89, 85, 70])
final_scores = np.array([67, 55, 92, 80, 79])

#1. Print the shape and data type of each array.
print("hours:  shape", np.shape(hours), "data type: ", hours.dtype)
print("attendance:  shape", np.shape(attendance), "   data type: ", attendance.dtype)
print("prev_scores:  shape", np.shape(prev_scores), "   data type: ", prev_scores.dtype)
print("final_scores:  shape", np.shape(final_scores), "   data type: ", final_scores.dtype)

#2. Find the mean final score.
mean_final_scores = np.mean(final_scores)
print("Mean of final scores:", mean_final_scores)

#3. Find the maximum and minimum final scores.
max_final_scores = np.max(final_scores)
print("Max of final scores:", max_final_scores)
min_final_scores = np.min(final_scores)
print("Min of final scores:", min_final_scores)

#4. Find the standard deviation of the final scores.
standard_deviation_final_scores = np.std(final_scores)
print("Standard deviation of final scores:", standard_deviation_final_scores)

#5. Add 5 bonus marks to each student's final score.
final_scores += 5
print("Final scores after giving 5 bonus marks:", final_scores)

#6. Create a Boolean array showing which students scored at least 75.
atleast_75 = final_scores >= 75

#7. Use Boolean indexing to print only the scores greater than or equal to 75.
greater_than_75 = final_scores[final_scores >= 75]
print("Students with final scores greater than or equal to 75:", greater_than_75)
