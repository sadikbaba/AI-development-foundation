import time

import numpy as np

# list
numbers_list = list(range(1_000_000))
numbers_array = np.array(numbers_list)

# python loop
start = time.perf_counter()
loop_result = []
for number in numbers_list:
    loop_result.append(number * 2)
loop_time = time.perf_counter() - start


# numpy
start = time.perf_counter()
array_result = numbers_array * 2
numpy_time = time.perf_counter() - start


print("Python loop:", loop_time)
print("NumPy:", numpy_time)
