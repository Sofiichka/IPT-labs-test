#description
#by Baltazar1697
def Fib(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return Fib(a-2)+Fib(a-1)
