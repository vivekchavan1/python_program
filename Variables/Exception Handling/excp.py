# try:
#     x = int(input("Enter the number:"))
#     result = 10 / x
#     print("Result",result)

# except ZeroDivisionError:
#     print("Error:you cannot divide by zero.")


# #Raising an Exception Inside a Condition

# age = int(input("Enter your age:"))

# if age < 0:
#     raise ValueError("Age Cannot Be Nagative!")

# else:
#     print("Your age is:",age)


#Raising an Exception Inside try–except

try:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        raise Exception("Number must be positive!")
    print("Good number:", number)

except Exception as e:
    print("Error:", e)
