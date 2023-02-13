import sys
import json
import timeit
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def func1(arr):
    def func2(array, start, end):
        p = array[start]
        low = start + 1
        high = end
        while low <= high:
            if array[high] >= p:
                high = high - 1
            else: 
                if array[low] <= p:
                    low = low + 1
                else:
                    array[low], array[high] = array[high], array[low]
        array[start], array[high] = array[high], array[start]
        return high
    def sorting(arr, low, high):
        if low < high:
            pi = func2(arr, low, high)
            sorting(arr, low, pi-1)
            sorting(arr, pi + 1, high)

    sorting(arr, 0, len(arr) - 1)


f = open(r"ex2.json", "r")

json_file = json.load(f)

length = len(json_file)

time_series=[]
num_array=[]


for i in range(length):

    num_array.append(i+1)
    array = json_file[i]
    time = timeit.timeit(lambda:func1(array), number = 1, globals = globals())
    time_series.append(time)
    print(time)

plt.plot(time_series, num_array, color = 'b')
plt.show()