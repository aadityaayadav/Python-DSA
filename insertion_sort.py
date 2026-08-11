num = [5, 7, 2, 4, 1, 3]

n = len(num)

for i in range(1, n):
    key = num[i]
    j = i - 1

    while j >= 0 and key < num[j]:
        num[j + 1] = num[j]
        j -= 1

    num[j + 1] = key
print(num)