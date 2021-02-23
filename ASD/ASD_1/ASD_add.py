n1 = int(input("Input number: "))
def number(n):
    if n!=0:
        print(n%10)
        n = n//10
        number(n)
number(n1)

n2 = int(input("Input another number: "))
def degree(n):
    if n == 1:
        return n
    else:
        return n* degree(n-1)