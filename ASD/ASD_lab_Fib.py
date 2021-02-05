#description
#by Baltazar1697
a = int(input('Input which number of Fibonacci you want to know '))
def Fib(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return Fib(a-2)+Fib(a-1)
print(Fib(a))