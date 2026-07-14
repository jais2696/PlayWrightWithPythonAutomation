#WAP to ind the greatest of 3 number entered by the user?

num1 = int(input("Enter a 1st number:"))
num2 = int(input("Enter a 2nd number:"))
num3 = int(input("Enter a 3rd number:"))
# lit=[num1,num2,num3]
# max=lit[0]
# i=0
# maxIdx=0

# while i < len(lit):
#     if max < lit[i]:

#         max = lit[i]
#         maxIdx= i
#     i += 1

#check which number is greater
if num1 >= num2 and num1 >= num3:
    greatest = num1

elif  num2 >= num1 and num2 >= num3:
    greatest = num2

else:
    greatest = num3

print("The greatest number is:", greatest)

