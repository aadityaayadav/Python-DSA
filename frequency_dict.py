num = [4, 2, 1, 1, 5, 4, 2, 8]
freq = {}

for i in range(0, len(num)):
    if num[i] in freq:
        freq[num[i]] += 1
    else:
        freq[num[i]] = 1

for num, i in freq.items():
    print(num, ":", i)
