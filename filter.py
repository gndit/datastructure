def odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    filt = (even,odd)
    print(filt)


s1 = [1,2,3,4,5,6,7,8,9,11]
odd_even(s1)
