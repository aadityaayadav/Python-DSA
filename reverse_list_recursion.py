
n= [1,2,3,4,5,6,7,8,9,10] 

def func(n, first, last):
    if first >= last:
        return 

    n[first], n[last] = n[last], n[first]
    func(n, first + 1, last - 1)

func(n, 2, 7)

print(n)