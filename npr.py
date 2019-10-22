def fact(a):
    if a<=0:
        return 1
    else:
        return fact(a-1)*a

def NPR(n,r):
    N=fact(n)
    R=fact(r)
    return N/R

print(NPR(5,2))