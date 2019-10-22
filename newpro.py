no = 17
count=0
for i in range(2, no//2):
    if no%i == 0:
        count = 1
        break
if count == 1:
    print("non prime")
else:
    print("prime")




