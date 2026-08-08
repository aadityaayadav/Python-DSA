


n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Step 1: Frequency store karo
freq = {}

for num in n:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Step 2: m ke elements ki frequency print karo
for num in m:
    if num in freq:
        print(num, "->", freq[num])
    else:
        print(num, "->", 0)        