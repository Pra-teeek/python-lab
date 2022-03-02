x= input("Enter any value: ")
if x.isdigit():
    print("User input is an Integer ")
    x=int(x)
    temp=x
    rev=0
    while(x>0):
       dig=x%10
       rev=rev*10+dig
       x=x//10
    if(temp==rev):
       print("Yes! The Number is a Palindrome!")
    else:
       print("No! The Number is not a Palindrome!")
else:
    print("User input is a String ")
    s=x
    y=s[::-1]
    if s==y:
      print("Yes! String is a Palindrome!")
    else:
      print("No! String is not a Palindrome!")