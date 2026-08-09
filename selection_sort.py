num = [5, 4, 7, 3, 1]

def selection_sort(num):
    n = len(num)

    for i in range(n):
        min = i

        for j in range(i + 1, n):
            if num[j] < num[min]:
                min = j

        num[i], num[min] = num[min], num[i]


selection_sort(num)
print(num)    



num = [5, 4, 7, 3, 1]

def selection_sort(num):
    n = len(num)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if num[j] > num[max_index]:
                max_index = j

        num[i], num[max_index] = num[max_index], num[i]


selection_sort(num)
print(num)