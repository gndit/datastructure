'''armstrong no 153
1qube + 5 qube + 3qube'''

no =153
temp=no
sum = 0
rem = 0
while temp!=0:
    rem = temp%10
    sum = sum+rem**3
    temp = temp//10

if no==sum:
    print("armstronge number")

else:
    print('not armstronge number')
    
'''
no =10
no=no**3
print(no)
'''