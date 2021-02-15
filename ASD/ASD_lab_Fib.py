#description
#by Baltazar1697
a = int(input('Input which number of Fibonacci you want to know '))
sum = 0
def Fib(a):
    global sum
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        sum = Fib(a-2)+Fib(a-1)
        return sum
print(Fib(a)-1)