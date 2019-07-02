import platform
import random
print("please input a number")
R=input()
i=0
if R.isdigit():
    while i< int(R):
      for x in range(int(R)):
          print(random.randint(1,10), end=' ') 
      print("\n")
      i+=1
else:
    while R!=int():
        print("please try again, input a number")
        R=int(input())
        if R > 0:
           i=0
           while i< int(R):
               for x in range(int(R)):
                  print(random.randint(1,10), end=' ') 
               print("\n")
               i+=1
        else:
            if R<=0:
                break
 