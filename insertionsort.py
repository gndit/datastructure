
def fun(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j] = key

            
    return a

l = [1,2,34,3,6,58,8,16]
print(fun(l))