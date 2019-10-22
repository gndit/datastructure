a=[1,34,64,7,8,5,83]
first_lar=-1
second_lar=-1
for i in a:
    if i > first_lar:
        second_lar = first_lar
        first_lar = i
    elif i < first_lar and i > second_lar:
        second_lar = i
print("first largest no : ",first_lar,"\nsecond largest no : ", second_lar)


print(max(a))
