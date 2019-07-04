import platform
s = "a"
while s == "a":
  print("Please input a number grater than 0")
  try:  
    n=int(input())
    if n > 0:
        s = "b"
    else:
        print(f"I requested yo to enter number grater than 0 and You entered {n}")
  except:
    print("Very funny, You have to enter a number")  

L=n
s=L-n
d=n*2-1
while n > 0:
 print(" "*s,"."*d)       
 n=n-1
 s=L-n
 d=n*2-1
