#WAP to take an age as input and print whether the person is "child"(age <13), or an "Adult"(age>=20)?

age= int(input("Enter your age: "))
if age <= 13:
    print("The person is child")
elif  age <= 20:
    print("The person is teenager")
else:
    print("The person is adult")
