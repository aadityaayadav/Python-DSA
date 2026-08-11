nums = [55, 45, 78, 12, 89, 34]

largest = nums[0]
n = len(nums)

for i in range(1, n):
    if nums[i] > largest:
        largest = nums[i]

print("The largest element in the array is:", largest)