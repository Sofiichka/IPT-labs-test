n1 = int(input("Input number: "))
def number(n):
    if n!=0:
        print(n%10)
        n = n//10
        number(n)
number(n1)