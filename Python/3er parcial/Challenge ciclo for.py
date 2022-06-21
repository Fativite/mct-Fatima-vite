import random
while True: 
 base="abcdefghijklmnñopqrstuvxyz"

passw="hello"
m=int(input("how long you want your password to be?:"))
for i in range (m):
  passw=passw+random.chioce(base)
  
print ("password",passw)
input()
  

