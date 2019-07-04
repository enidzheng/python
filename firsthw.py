import platform
#def pyramid():
print("please input a number")
try:
    n = int(input())
    #print (f"your input is int {n}")
    if (n>0): 
    #print("Your input is number")
      L=n
      L = int(L)
      s=L-n
      d=n*2-1
      while n > 0:
       print(" "*s,"."*d)       
       n=n-1
       s=L-n
       d=n*2-1
    elif (n<=0):
      print("please input a positive number")
     
except ValueError:
    print("That's not an int!, pleas try again")
   
#n=int(n)
'''if (n>0): 
    #print("Your input is number")
    L=n
    L = int(L)
    s=L-n
    d=n*2-1
    while n > 0:
      print(" "*s,"."*d)
      n=n-1
      s=L-n
      d=n*2-1
elif (n<=0):
    print("please input a positive number")
else:
     print("your input is string, please try again")'''
 
  
