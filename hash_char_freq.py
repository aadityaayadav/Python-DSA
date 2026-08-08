

m = "abcdakklbdcadabfeada"
n = ['a', 'b', 'c', 'd']

# Step 1: Frequency store karo
freq = {}

for ch in m:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: m ke elements ki frequency print karo
for ch in n:
    if ch in freq:
        print(ch, "->", freq[ch])
    else:
        print(ch, "->", 1)   