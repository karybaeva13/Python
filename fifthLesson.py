age = input("enter your age: ")
education = input("Do you have a degree? ")

try:
    age = int(age)

    if age > 0 and age < 6 and education == "no":
        print("This is a preschool")

    elif age >= 6 and age <=18 and education == "no":
        print("This is a school student")

    elif age >= 6 and age <=18 and education == "yes":
        print("This is a college student")

    elif age >18 and education == "yes" or age >18 and education == "no":
        print("This person does not study in school")

except:
    print("The information is not defined")

finally:
    print("The operation is completed")