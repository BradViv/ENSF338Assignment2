



def fib(n, fib_dict = {}):

    if n == 0 or n == 1:
        return n
    else:
        if n in fib_dict:
            return fib_dict[n]
        else:
            fib_dict[n] = (fib(n-1) + fib(n-2))
            return fib_dict[n]
