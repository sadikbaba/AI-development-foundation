import pandas as pd

students = pd.read_csv("data/students.csv")
print(students)
print("\n")

fill_nan =students.fillna(0)
print(fill_nan)

print("\n")
print(fill_nan.describe())


# drop duplicates
students = pd.read_csv("data/students.csv")
clean_students = students.drop_duplicates()
print("\n")
print(clean_students)

#  head
print("\nHead")
head_students = students.head() # first 5 rows by default
print("\n5 students by default" )
print(head_students)
head_students = students.head(3) # first 3 rows
print("\nhead 3 students")
print(head_students)

# info 
print("\ninfo")
students.info()



