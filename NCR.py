
def fact(a):
    if a<=0:
        return 1
    else:
        return fact(a-1)*a


def ncr(n,r):
    n1=fact(n)
    r1=fact(r)
    t=fact(n-r)
    return n1/(r1*t)

print(ncr(6,3))

'''
''using pascal rule''

def ncr(n,r):
    if n==0 or n==r:
        return 1
    else:
        return ncr(n - 1, r - 1) + ncr(n - 1, r)



print(ncr(4,2))
'''