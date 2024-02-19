#   Part4- Conditional statements

"""It includes 
1) If- Else statement
2) Nested-if statement"""

#  Basic Program on if else statement

# num = int(input("Enter a number : "))
# if(num>=10):
#     print("Hello")
# else:
#         print("Hii...")


#  Basic program of if else if statement

# age = int(input("Enter a age : "))

# if(age>=2):
#     print("Kids ")
# elif(age>=7):
#     print("Child")
# elif(age>=13):
#     print("Adult")
# elif(age>=18):
#     print("Young")
# else:
#     print("Old")


#  Basic program on Nested if statement

# Asking user's age
age = int(input("Enter your age: "))

#Checking age
if age >= 18:
    print("You are eligible to vote.")
    if age >= 65:
        print("You are also eligible for senior citizen benefits.")
else:
    print("You are not eligible to vote yet.")




