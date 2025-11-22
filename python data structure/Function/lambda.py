n = lambda x:x+10
print(n(10))

n = lambda x,y:x*y
print(n(2,10))

n = lambda x:"zero" if x==0 else "Even" if x % 2==0 else "Odd"

print(n(5))

print(n(8))

print(n(0))


n = [lambda a = x: a * 10 for x in range(1, 6)]
for i in n:
    print(i())


#Lambda with multiple statements

calculation = lambda a,b :(a + b, a - b, a * b, a / b, a % b)

ans = calculation(3,4)
print(ans)


#using lambda with filters
 
num = [1,2,3,4,5,6,7]

is_even = filter(lambda a : a % 2==0,num)

print(list(is_even))


#using lambda with map()

num = [1,2,4,6,8]

square = map(lambda a : a ** 2,num)

print(list(square))


#using lambda with reduce()
from functools import reduce
num_list = [2,0,2,5]

number = reduce(lambda x,y : x * 10 + y,num_list)

print(number)