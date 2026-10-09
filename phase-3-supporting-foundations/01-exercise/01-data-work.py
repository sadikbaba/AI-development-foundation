number = [1, 2, 3, 4, 5]

for i in range(len(number)):
    print(number[i])


#  in data work you will simply write a loop in one line
print("\n")
[print(number[i]) for i in range(len(number))]


# you can also do filter
print("\n")
i = [number[i] for i in range(len(number)) if number[i] > 2]
print(i)
