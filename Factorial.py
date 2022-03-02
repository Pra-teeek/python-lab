def fac(x):
    if x == 1:
       return x
    else:
       return x*fac(x-1)
    
x=int(input('Enter a Number: '))

if x < 0:
   print("Factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1")
else:
   a=fac(x)
   print('Factorial of {} is {}'.format(x,a))

 # for i in range(1,x):
       # x=x*fac(x-1)

        # return x