import calculator_1 as c

print("1.add")
print("2.sub")
print("3.mult")
print("4.div")

select = int(input("select operation 1-4 : "))
a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2: "))

if select == 1:
    print(c.add(a,b))

elif select == 2:
    print(c.sub(a,b))

elif select == 3:
    print(c.mult(a,b))

elif select == 4:
    print(c.div(a,b))   

else:
    print("Invalid input")