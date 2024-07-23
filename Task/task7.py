alphs=[0]*26

name = input()
name=name.upper()
for i in name:
    alphs[ord(i)-65]+=1

for i in range(0,len(alphs)):
    if  alphs[i]!=0:
        print(alphs[i],chr(i+65))