def selection(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min] :
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    return a

l = [1,11,23,2,4,69,6]
print(selection(l))