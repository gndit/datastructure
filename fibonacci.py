'''0,1,1,2,3,5,8,13 fibonacci series'''
'''
a=0
b=1
num = int(input("enter a no : "))
print(a,b, end=' ')
for i in range(num):
    c=a+b
    print(c, end=' ')
    a=b
    b=c
    '''

def fib(n):
    if n<=1:
        return n
    return fib(n-2)+fib(n-1)

print(fib(5))