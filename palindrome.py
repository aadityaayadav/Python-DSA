lst = "abcba"

n= len(lst)
left=0
right= n-1

while left<right:
    if lst[left]!=lst[right]:
        print("Not a palindrome")
        break
    left+=1
    right-=1

else:
    print("Palindrome")