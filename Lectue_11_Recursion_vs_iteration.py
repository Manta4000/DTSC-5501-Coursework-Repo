### 9.29.2026
### 1) Implementing a Recursion and iterative factorial

x = 10
### Recursive function
def final_(x):
    if x == 0:
        return 1
    else:
        return x*final_(x-1)

### Iterative factorial

def iterative_(x):
    final = 1
    for i in range(2, x+1):
        final *= i
    return final, print(final)

### Test both

final_(x)

iterative_(x)

### 2) Implementing recursive and iterative fibonacci

def fib(n):
    if n <=1:
        n, n-1
    return fib(n-1) + fib(n-2)

fib(50)

def fib2(n, m):
    n, m = 0,1
    for i in range(x):
        n, m = m, n+m
    return m


