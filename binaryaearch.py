def binary(a,n):
    l=0
    h=(len(a))-1
    mid = (l+h)//2
    flage=0
    while l<=h :
        if a[mid]==n :
            print("item found at position ",mid+1)
            flage=1
            break
        elif a[mid]<n :
            l = mid+1
        else:
            h= mid-1
        mid = (l+h)//2
    if flage==0:
        print("item not found")

l = [12,14,21,25,34,40,78,89,99,100]
print(binary(l,23))

