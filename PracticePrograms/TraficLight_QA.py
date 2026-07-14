#WAP to take a traffic light color (Red,Yellow,Green) as input and prints the action required (Stop,Look,Go)

Light = input("Enter traffic light color: ")

if Light == "Red":
    print("Action: Stop" )
elif Light == "Yellow":
    print("Action: Look")
elif Light == "Green":
    print("Action: Go")
else:
    print("Invalid color entered!")    
    

