l=[1,3,6,4,7]
def fu(a):
    for i in a:
        yield i

b=fu(l)
for i in range(len(l)):
    print(next(b))

print(next(b))
