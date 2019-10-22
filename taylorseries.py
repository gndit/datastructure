'''
def e(x,n):
    s=1
    while n>0:
        s=1+(x*s)/n
        n-=1
    return s

print(e(8,5))
'''
'''

def exponent(x,n):
    s=1
    if n==0:
        return s
    s=1+(x*s)/n
    return exponent(x,n-1)
print(exponent(2,5))
'''

result = 0
def e(x,n):
    f=1
    p=1
    if n==0:
        return 1
    else:
        result = e(x,n-1)
        p=p*x
        f=f*n
        return result+p/f
print(e(6,7))
