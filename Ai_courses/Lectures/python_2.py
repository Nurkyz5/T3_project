# ======Decimal======
#  first, we should import it

from decimal import Decimal
a=Decimal('0.1')
print(a+a+a+a+a+a+a+a+a)


# binary - in binary system
a=bin(10)
print(a)
print(int(a,2))

# hex (16 system)
b=hex(10)
print(b) #0xa


# complex numbers - (2j+3+2k)
a=complex(1,5)
print(a)

"""===============Operations with numbers"""


# Modules
print(abs(-5))

# Round
print(round(12.6))

# sqrt
from math import sqrt
print(sqrt(25))

# pow
# 1)
print(pow(5,3))
# 2)
print(pow(2,3,5))

# divmod
# it's a function which returns 2 numbers, 1st - whole numbers, 2nd - ostatok
print(divmod(10,3))



'==========Practice=============='
# 1.


a=5
b=9

# math
# a=a+b
# b=a-b
# a=a-b
# print('a: ',a, ",b: ",b)

# python
a,b=b,a
print('a: ',a, ",b: ",b)



# 2 
# We are to run only the lust number

a=438
last_digit=a%10
print(last_digit)

# We are to run the predposl number

a=452
digit=a%100
print(digit//10)

# How many minutes
seconds=367
print(seconds//60)
print(seconds%60)

# Перевернуть число

num=123
num1=num//100
num2=num%100//10
num3=num%100%10

print(num3*100+num2*10+num1)