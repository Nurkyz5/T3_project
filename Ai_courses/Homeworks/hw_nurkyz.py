

#Task_1

for i in range(7):
    print("java",end=",")
     


     
#Task_2======

user_input = input("Write a word and a number by tab: ")
while input!='stop':
  word,number=user_input.split(" ")
  print(word)
  print(number)

     


     
#Task_3

i=range(2,14)
for a in i:
  print(a)

     


     
#Task_4

i=range(2,14)
num_list=[a for a in i]
print(num_list)
     


     
#Task_5

num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
for i in num_list:
  if i%2==0:
    print(i)
     


     


     
#Task_6

num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
for i in num_list:
   if i%2==1:
      num_list.remove(i)
print(num_list)



num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
for i in num_list:
   if i==1 or i==3 or i==5 or i==7 or i==9:
      num_list.remove(i)
print(num_list)
     


     
#Task_7

numbers=list(range(4,22))
print(numbers)
sum_=0
for number in numbers:
    if number%2==1:
        sum_+=number
print(sum_)



     


     
#Task_8

num = list(range(int(input("Write a number and I'll find the sum from 1 to this number: "))))
sum_=0
for i in num:
   sum_+=i+1
print(sum_)

     


     
#Task_9

num=int(input("Write the number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)



     
#Task_10

n=int(input("Write the number: "))
res=0
for i in range(1,1+n):
    res+=i**2-i
print(res)


     
#Task_11

x = [1, 3, 4, 3, 5, 7, 7, 4, 8, 2, 9, 10, 2, 1, 0]
x_=sum(x)/len(x)
dx=0
for i in x:
    dx+=(i-x_)**2
print(dx)
     


     


     
#Task_12

str_ = 'Ты виноват лишь в том, что хочется мне кушать...'
for i in str_:
  print(i)
word=str_.split()
for i in word:
  print(i)

     


     
#Task_13

str_ = 'kjhkj4323kk43kbh543t5'
result=[i for i in str_ if not i.isdigit()]
print(result)
     


     
#Task_14

word_list = ['apple', 'mountain', 'astronomy', 'aerobic', 'river', 'ant',
             'airplane', 'ocean', 'art', 'alpine', 'guitar', 'atom',
             'dog', 'alligator', 'sun', 'astral', 'box', 'amplifier']
word_list=[word.title() for word in word_list]
print(word_list)
    

     


     
# Task_15
word_list = ['apple', 'mountain', 'astronomy', 'aerobic', 'river', 'ant',
             'airplane', 'ocean', 'art', 'alpine', 'guitar', 'atom',
             'dog', 'alligator', 'sun', 'astral', 'box', 'amplifier']

word_with_a=[word for word in word_list if word.startswith('a')]
print(word_with_a)

     


     
#Task_16

user_id = [21, 23, 245, 663, 435, 609, 906, 9843]
for i in user_id:
  print(f"ID_{i}")
     


     


     
#Task_17

num_list = [5, 21, 23, 245, 663, 435, 609, 906, 9843]
for i in num_list:
   i=str(i)
   if len(i)==1:
      print(f'000{i}')  
   elif len(i)==2:
      print(f'00{i}')
   elif len(i)==3:
      print(f'0{i}')
   else:
      print(i)


     


     
#Task_18

DNA = 'AATTAGGATGATCGCTAGGCTCGATAGGCTAGTTCCGGGAGCTGACTGC'
mapping={
    'A':'U',
    'G':'C',
    'T':'A',
    'C':'G'
  }
RNA=''.join(mapping[i] for i in DNA)
print(RNA)


     


     
#Task_19

DNA = 'AATTAGGATGATCGCTAGGCTCGATAGGCTAGTTCCGGGGGGGAGCTGACTGC'
A=DNA.count("A")
C=DNA.count("C")
G=DNA.count("G")
T=DNA.count("T")

if A>C and A>G and A>T:
        print(A)
elif C>A and C>G and C>T:
        print(A)
elif G>C and G>A and G>T:
        print(A)
elif T>C and T>G and T>A:
        print(A)
        


     


     
#Task_20

str_ = 'ABBCABACBGBCABCGBBCBAGABCBACGF'
unique=[]
str_=list(str_)
for i in str_:
    if i not in unique:
        unique.append(i)
print(unique)

     
#Task_21


str_ = 'ABCABABBCABCGBACBGACFBBBBCCCCBCCCBCCCCGCCCABCCCBAACBCCCCCC'
letters = ['A', 'B', 'C', 'G', 'F']
max_letter = max(letters, key=str_.count)
print(max_letter)



str_ = 'ABCABABBCABCGBACBGACFBBBBCCCCBCCCBCCCCGCCCABCCCBAACBCCCCCC'
A=[]
B=[]
C=[]
G=[]
F=[]

str_=list(str_)
for i in str_:
    if i=='A':
        A.append(i)
    elif i=='B':
        B.append(i)
    elif i=='C':
        C.append(i)
    elif i=='G':
        G.append(i)
    elif i=='F':
        F.append(i)
if len(A)>len(B) and len(A)>len(C) and len(A)>len(F) and len(A)>len(G):
    print(A[0])
elif len(B)>len(A) and len(A)>len(C) and len(A)>len(F) and len(A)>len(G):
    print(B[0])
elif len(C)>len(B) and len(C)>len(A) and len(A)>len(F) and len(A)>len(G):
    print(C[0])
elif len(G)>len(B) and len(A)>len(C) and len(A)>len(F) and len(G)>len(A):
    print(G[0])
elif len(F)>len(B) and len(A)>len(C) and len(F)>len(A) and len(A)>len(G):
    print(F[0])
   


     
#Task_22

x=list(range(-1000,1000))
y=0
for i in x:
    y=i**2+4*i-12
    if y==0:
        print(i)
   


     


     
#Task_23

value=[]
for x in range(-100,100):
    y_temp=x**2-4*x-3
    value.append(y_temp)
print(min(value))



     
#Task_24

value=[]
for x in range(-100,100):
    y_temp=x**2-4*x-3
    value.append(y_temp)
y_min=min(value)
for x in range(-100,100):
    if x**2-4*x-3==y_min:
        print(x)



     


     
#Task_25

x=1.0
while x<=3.0:
    print(round(x,1))
    x+=0.1
     
#Task_26

sum_=[]
x = [1, 2, 3, 4, 5, 4]
y = [4, 5, 4, 6, 8, 9]
for i in range(len(x)):
    xi=x[i]
    yi=y[i]
    summ=xi+yi
    sum_.append(summ)
print(sum_)
     

     


     
#Task_27

z=[]
x = [-3, -2, 1, 3, 5, 6]
y = [0, 3, 4, -2, 4, 1]
for i in range(len(x)):
    xi=int(x[i])
    yi=int(y[i])
    zi=2*xi+0.1*yi**2-5
    z.append(zi)
print(z)

     


     
#Task_28

lat = [42.424, 43.345, 41.425, 42.356, 44.653, 41.453]
lon = [63.989, 64.996, 71.654, 72.356, 69.836, 70.909]
coord=[]
for i in range(len(x)):
    lati=lat[i]
    loni=lon[i]
    ci=lati,loni
    coord.append(ci)
print(coord)
     


     


     
#Task_29

best_h=0
best_a=0
min_s=float('inf')
h=0.1

while h<=32:
    a=(32/h)**0.5
    s=a**2+4*a*h
    if s<min_s:
        min_s=s
        best_h=h
        best_a=a
    h+=0.01
print("Оптимальная глубина:", round(best_h, 2))
print("Сторона дна:", round(best_a, 2))
print("Минимальная площадь облицовки:", round(min_s, 2))
     
houses = {
    "house_1": "Продаю дом с большим участком 8 соток. На участке имеется газ, свет.",
    "house_2": "Продается дом с ровным участком, Красная книга, газ, вода, телефон все вопросы - звоните отвечу, здравствуйте!",
    "house_3": "Продаю ровный дом с остекленным участком, вода есть в наличии водопровод звоните 89 млн сом.",
    "house_4": "Здравствуйте! Продается большой дом из 29 комнат. Хорошо проживать большой семьей с видом на горы.Присутствует газ и вода. Документы КРАСНАЯ книга, тех паспорт, договор купли продажи звоните"
    }

features = ["свет", "вода", "красная книга"]

result = {}

for name, text in houses.items():
    text = text.lower()
    row = []
    
    for feature in features:
        if feature in text:
            row.append(1)
        else:
            row.append(0)
    
    result[name] = row

print(result)
