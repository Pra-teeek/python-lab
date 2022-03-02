def swap(x,y): 
    x,y=y,x
    return x,y 

a=int(input('Enter value a : '))
b=int(input('Enter value b: '))    
a,b=swap(a,b) 
print('After swapping a becomes :',a)
print('After swapping b becomes :',b)