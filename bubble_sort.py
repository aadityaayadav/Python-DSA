def bubble_sort(num):
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
num = [5, 2, 9, 1, 5, 6]

n = len(num)

bubble_sort(num)
print(num)
