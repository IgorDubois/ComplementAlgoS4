import time

values = {0 : 0 , 1 : 1}

def fibonacci(n):
    if n < 0:
        exit(2)
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_with_tab(n):
    global values
    if n < 0:
        exit(2)
    if n in values:
        return values[n]
    else:
        i = fibonacci_with_tab(n-1)+fibonacci_with_tab(n-2)
        values[n] = i
        return i

def fib_paire(n):
    if n == 1:
        return (1,0)
    else:
        (x,y) = fib_paire(n-1)
        return (x+y , x)

i = 999

"""
start_time = time.time()
#n = int(input("n ? > "))
print "Fibonacci de " + str(i) + " = " + str(fibonacci(i))
print time.time() - start_time
print ""
"""

start_time = time.time()
#n = int(input("n ? > "))
n = fibonacci_with_tab(i)
print time.time() - start_time
print "Fibonacci de " + str(i) + " = " + str(n)
print str(len(str(n))) + " caracteres"
print ""
print values

start_time = time.time()
#n = int(input("n ? > "))
n = fib_paire(i)
print time.time() - start_time
print "Fibonacci de " + str(i) + " = " + str(n)
print str(len(str(n))) + " caracteres"
print ""
