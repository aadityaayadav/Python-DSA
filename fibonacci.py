
def fib(num: int) -> int:
    if num <= 1:
        return num
    else:
         return fib(num - 1) + fib(num - 2)

print(fib(7))    