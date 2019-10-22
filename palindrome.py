num = 125
temp=num
rem = 0
rev = 0
while temp!=0:
    rem = temp%10
    rev = rev*10 + rem
    temp = temp//10
if (rev==num):
    print('palindrome')
else:
    print('not palindrome')

