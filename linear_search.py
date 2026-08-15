nums = [5, 9, 1, 7, 3, 15]

target = 7
n = len(nums)

result = -1

for i in range(n):
    if nums[i] == target:
        result = i
        break

print(result)