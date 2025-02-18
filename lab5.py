import statistics

# Task 4: Analyzing grades from a list of numbers

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Convert the data string into a list of integers (grades)
grades = list(map(int, data.split(',')))

# Output the list of grades
print("Grades:", grades)

# Calculate the minimum and maximum grade
min_grade = min(grades)
max_grade = max(grades)

# Output the min and max grade
print(f"Minimum grade: {min_grade}")
print(f"Maximum grade: {max_grade}")

# Calculate the average grade
average_grade = round(sum(grades) / len(grades), 2)

# Output the average grade
print(f"Average grade: {average_grade}")

# Calculate the mean grade using statistics library
mean_grade = round(statistics.mean(grades), 2)

# Output the mean grade
print(f"Mean grade: {mean_grade}")

# Calculate the median grade using statistics library
median_grade = statistics.median(grades)

# Output the median grade
print(f"Median grade: {median_grade}")

# Format and output all the results
output = (
    f"Minimum grade: {min_grade}\n"
    f"Maximum grade: {max_grade}\n"
    f"Average grade: {average_grade}\n"
    f"Mean grade: {mean_grade}\n"
    f"Median grade: {median_grade}"
)

print(output)
