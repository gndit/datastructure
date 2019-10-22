class Boy:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
print("enter your fname lname and age ")
first_name=input("enter your name :")
last_name=input("enter your lastname :")
ag=input("enter your age")
A = Boy(first_name,last_name,ag)

print(A.f_name)
print(A.l_name)
print(A.age)