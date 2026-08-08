n = 153
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    ld = temp % 10
    total += ld ** digits
    temp //= 10

# if total == n:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

print(total)