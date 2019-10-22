def bubble(b):
    for i in range(len(b)):
        for j in range(len(b)-1-i):
            flage = 0
            if b[j]>b[j+1]:
                temp = b[j]
                b[j]=b[j+1]
                b[j+1]=temp
                flage = 1
        if flage==0:
            break
    return b

l=[3,42,546,6,74,7,34]
print(bubble(l))



