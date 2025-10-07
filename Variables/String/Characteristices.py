

#Accessing Characters
V = "Welcome to Icon"

print("Datatype:",type(V))

print("V[0]:",V[0])
print("V[6]:",V[6])


#String Slice

print("V[5:]:",V[5:])
print("V[:5]:",V[:5])
print("V[2:7]:",V[2:7])
print("V[-3::]:",V[-3::])

#Updating String

string_1 = "welcome to icon"
print("string_1:",string_1)

new_str_1 ="W" + string_1[1:] 
print("new_str_1:",new_str_1)

new_str_2 = string_1.replace("icon","to yard")
print("new_str_2:",new_str_2)


#strip
#remove and replace

str_1 = "      virat      "  
print("String 1:", str_1)

# removing spaces from both ends  
print("After removing spaces from both ends:")  
print(str_1.strip())

str_2 = "Learning Python with TpointTech is fun!"  
print("String 2:", str_2)


# replacing 'fun' with 'amazing'  
print("After replacing 'fun' with 'amazing':")  
print(str_2.replace("fun", "amazing"))