UserAge = int(input("Enter Your Age :"))

if UserAge < 2:
    print("The Person is a Baby")
elif UserAge >= 2 and UserAge < 4:
    print("The Person is a Toddler")
elif UserAge >= 4 and UserAge < 13:
    print("The Person is a Kid")
elif UserAge >= 13 and UserAge < 20: 
    print("The Person is a Teen")
elif UserAge >= 20 and UserAge < 65:
    print("The Person is an adult")
else:
    print("The Person is an Elder")
 
