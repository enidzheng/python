import platform
import random
import traceback
print("please input a number")
R=input()
i=0
try:
    while R.isdigit() == True:
      while i< int(R):
        for x in range(int(R)):
          print(random.randint(1,10), end=' ') 
        print("\n")
        i+=1
      print ("please input a number big than 0")
      R = input ()
except Exception as e:
     print("type error: " + str(e))
     print(traceback.format_exc())
      # else:
      #   while R!=int():
      #      print("please try again, input a number")
      #      R=int(input())
      #      if R > 0:
      #         i=0
      #         while i< int(R):
      #            for x in range(int(R)):
      #              print(random.randint(1,10), end=' ') 
      #            print("\n")
      #            i+=1
      #      else:
      #        if R<=0:
      #           break