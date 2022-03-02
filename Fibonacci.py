def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

terms=int(input('Pls Enter a positive number of Terms: '))
print("Fibonacci sequence:")
for i in range(terms):
    print(fib(i))



