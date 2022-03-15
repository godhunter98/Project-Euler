x = 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)

# we keep adding every new even fib no. to find their sum upto 4mill!
   if z% 2 ==0:
    result += z
   
   
#for the next iteration, we make the new Fib number, the sum of last 2!
   x,y = y,z
print (result)

