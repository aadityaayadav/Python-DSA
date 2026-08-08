n = 100
fact= 1
total = 0
for i in range(1, n+1):
    if n % i==0:
        fact+=1
        print(i, end=" ") 
        total +=1
print ()
print (total)           
       
result = []
for i in range(1, n//2+1):
    if n % i==0:

        result.append(i)
result.append(n)
print(result)        