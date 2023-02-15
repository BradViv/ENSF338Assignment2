import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

f = open(r"ex2.json", "r")

json_file = json.load(f)

length = len(json_file)
time_series=[]
num_array=[]

for i in range(length):

    num_array.append(i+1)
    array = json_file[i]
    time = timeit.timeit(lambda:func1(array, 0, len(array) - 1), number = 1, globals = globals())
    time_series.append(time)
    print(time)
plt.plot(time_series, num_array, color = 'r')
plt.show()