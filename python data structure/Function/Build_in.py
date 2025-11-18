#Python abs() Function

integer = -20
print(abs(integer))

#python all() function used like And

V = [1,3,4,6]
print(all(V))

V = [0,False]
print(all(V))

V = [1,3,4,0]
print(all(V))

V = [0,False,5]
print(all(V))

V = []
print(all(V))

#bin() function

x = 10
print(bin(x))

y = 34
print(bin(y))

#bool() function

new = []
print(bool(new))

new = [0]
print(bool(new))

new = 0.0
print(bool(new))

new = None
print(bool(new))

new = True
print(bool(new))

new = 'easy string'
print(bool(new))

# #Compile code

# code_str = 'x=5\ny=10\nprint("sum =",x+y)'
# code = compile(code_str,'sum.py','exec')
# exec(code)
# exec(x)

#any() function (used like or)

V = [4,5,2,0]
print(any(V))

V = [0,False]
print(any(V))

#sum() function

s = sum ([1,3,5,3])
print(s)

s = sum([1,3,5],10)
print(s)