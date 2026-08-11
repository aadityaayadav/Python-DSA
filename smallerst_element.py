num =[55, 48, 78, 12, 89, 34]

smallest = float('inf')
second_smallest = float('inf')
n = len(num)



for i in range(n):
    if num[i] < smallest:
        smallest = num[i]

    elif num[i] < second_smallest and num[i] != smallest:
        second_smallest = num[i]    

print("The smallest element in the array is:", smallest)
print("The second smallest element in the array is:", second_smallest)