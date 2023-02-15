
import timeit
import matplotlib.pyplot as plt

def fib(n, fib_dict = {}):

    if n == 0 or n == 1:
        return n
    else:
        if n in fib_dict:
            return fib_dict[n]
        else:
            fib_dict[n] = (fib(n-1) + fib(n-2))
            return fib_dict[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

time_fib_old = []
time_fib_new = []

num_array = []

for i in range(0, 35):
    num_array.append(i+1)
    time_old = timeit.timeit(lambda:func(i), number = 1, globals = globals())
    time_fib_old.append(time_old)
    print(time_old)

    time_new = timeit.timeit(lambda:fib(i), number = 1, globals = globals())
    time_fib_new.append(time_new)
    print(time_new)


plt.plot(time_fib_old, num_array, color = 'b', label = "Old function")
plt.plot(time_fib_new, num_array, color= 'r', label = "New function")
plt.legend()
plt.show()