#WAP to input two numbers and operator (+,-,/,*) to perform basic calculations based on user choice?

a = float(input("Enter 1st numbre: "))
b = float(input("Enter 2nd number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a+b)
elif operator == "-":
    print("Result:", a-b)
elif operator == "*":
    print("Result:", a*b)  
elif operator == "/":
    if b !=0:
        print("Result:", a/b)
    else:
        print("Result: Error not divisible by zero")
else:
    print("Invalid operator!")              