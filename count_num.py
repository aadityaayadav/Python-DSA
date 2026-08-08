nums = 5142446
count = 0

while nums > 0:
    count += 1
    nums = nums // 10

print("Number of digits:", count)      