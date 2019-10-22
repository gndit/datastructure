'''def unio(l1,l2):
    ans = []
    for i in l1:
        if i not in ans:
            ans.append(i)
    for num in l2:
        if num not in l1 and num not in ans:
            ans.append(num)
    print(ans)

a = [1,2,3,42,1,2,3,2,2,3,1]
b = [2,4,1,8,11,2,2,1,6,6,8,9,0]
unio(a,b)
'''
x = {1,2,3,4,5,6,7}
y = {2,3,4,1,6,7,8}
ans = x | y

print(ans)
