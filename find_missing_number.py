nums = [1, 2, 3, 5, 6, 7, 8, 9]

n = len(nums)+1

for i in range(1, n+1):
    if i not in nums:
        print(i)
        break


missing = (n * (n + 1)) // 2 - sum(nums)

print(missing)