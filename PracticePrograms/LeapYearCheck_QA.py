#WAP to check if a year entered bu=y user is leap year or not.
# a year is leap year if it is divivble by 4 but century years like 1900 must also be divisible by 400

year = int(input("Enter a year: "))

if (year % 4 ==0 ) or (year % 400 ==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

           