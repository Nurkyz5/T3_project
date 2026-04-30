#=============Cycle==========

#it is a block of code which runs several time

#types of cycle: for, while
#list-[1,2,3], set, tuple, dict, str
#ends the work til the last element
#"range" generates numbers

#while is a cycle which work til True

for i in range(1,11):
    print(i)

n=1
while n<11:
    print(n)
    n+=1


#=============Key words in cycles======
#break stops cycle(cycle exit)
#continue - go to next iteration

for i in range(10):
    if i==3:
        continue
    print(i) 

for i in range(10):
    if i==5:
        break
    print(i)

while True:
    age=int(input("Write your age:"))
    if age<18:
        print("Write age above")
        break

string="hi hi ai academy".split(" ")

for letter in string:
    print(letter)

#==========Practice===========
#sum from 1 to 100

sum=0
for i in range(101):
    sum+=i
print(sum)

#1
for i in range(1,101):
    if i%2==0:
        print(i)

#2
for num in range(1,101):
    if num%2!=0:
        continue
    print(num)

#3
for num in range(2,101,2):
    print(num)

secret=7
while True:
    num=int(input("Write number: "))

    if num==secret:
        print("Harika1 You finded")
        break
    else:
        print("try again!")

secret_number=75
attempts=5
while attempts>0:
    num=int(input("Write number: "))

    if num<secret_number:
        print("Try again!")
        attempts-=1
    elif num>secret_number:
        print("Try again!")
        attempts-=1
    else:
        print("You won the game!")
        break
    if attempts>0:
        print("I believe in you!")
    else:
        print("You are cooked! There is no attempts!")

#Write calculator and while I write exit, program works


while True:
    num3=input("Write a number: ")
    if command in "+-*/":
        break
    else:
        print("Write correct operation")
    if num3=="exit":
        break
    num4=int(input("Write a number: "))
    if num4=="exit":
        break
    command=input("Choose operation(+,-,*,/): ")
    if command=="exit":
        break
    elif command=="+":
        print(int(num3)+int(num4))
    elif command=="-":
        print(int(num3)-int(num4))
    elif command=="*":
        print(int(num3)+int(num4))
    if num4=="0":
        print("We con divide to 0")
    else:
        print(int(num3)/int(num4))

num1=int(input(" "))
num2=int(input(" "))
action1=num1+num2
action2=num1-num2
action3=num1*num2
action4=num1/num2

player=input(f"Choose an operation")

