num = [55, 48, 78, 12, 89, 34]

largest = float('-inf')
second_largest = float('-inf')
n = len(num)

for i in range(n):
    if num[i] > largest:
        second_largest = largest
        largest = num[i]
    elif num[i] > second_largest and num[i] != largest:
        second_largest = num[i]

print("The second largest element in the array is:", second_largest)


        