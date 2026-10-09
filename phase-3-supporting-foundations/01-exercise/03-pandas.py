# pandas
import pandas as pd

data = {
    "name": ["Ali", "Sara"],
    "age": [20, 25],
}

df = pd.DataFrame(data, index=["student_a", "student_b"])

print(df)

print("\n")

print(df["age"])
print(type(df["age"]))

#  loc with index
print("\n")
print(df.iloc[1])

# loc with label
print("\n")
print(df.loc["student_a"])

#  filter
print("\n")


# using below i will filter the result from 70 to higher

scores = pd.DataFrame({
    "name": ["Ali", "Sara", "Musa"],
    "score": [55, 80, 70],
})

high_scores = scores[scores["score"] >= 70]
print(high_scores)


# group by 
print("\n")
students = pd.DataFrame({
    "class": ["A", "A", "B", "B"],
    "score": [60, 80, 70, 90]
})

average_score =students.groupby("class")["score"].mean()
print(average_score)



#  missing values
print("\n")
students = pd.DataFrame({
    "name": ["Ali", "Sara", "Musa"],
    "score": [80, None, 70]
})

print(students)
print("\n")
print(students.isna())

print("\n")
clean_students = students.dropna()
print(clean_students)