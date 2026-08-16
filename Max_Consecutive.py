nums = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1]

n = len(nums)
max_count = 0
count = 0


for i in range(n):
    if nums[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print(max_count)