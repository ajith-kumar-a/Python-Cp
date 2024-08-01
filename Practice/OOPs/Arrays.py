from array import *

vals = array('I',[1,2,3,4,5,6,7,87,8])

vals.reverse()

print(vals.buffer_info()) # (address = 2511664929872,size =  9)

print(vals)

for i in vals:
    print(i,end=", ")

newArray = array(vals.typecode, (a for a in vals))

print(newArray.typecode)

# _______________________________________________________________________________________________________________________________

arr = array('i',[])