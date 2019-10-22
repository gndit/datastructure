'''def common(l1,l2):
    same = []
    for num in l1:
        for i in l2:
            if num == i:
             same.append(i)

    print(same)
common([1,2,3,4,5],[2,4,5,6,78,9])
'''
x = {1,2,3,4,5,6,7}
y = {2,3,4,1,6,7,8}
ans = x & y

print(ans)
