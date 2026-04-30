#Task_1

list_ = ["I'm_str" for _ in range(11)] 

zeros = ['0' for _ in range(11)]

print(list_)
print(zeros)

     
#Task_2

num_list = [int(i) for i in range(1,16)]
print(num_list)
     


     
#Task_3

str_ = 'abcdefg12345ghi'

str_list = [i for i in str_]
print(str_list)

     
#Task_4

list_ = [str(i) for i in range(10,101,10)]
print(list_)
     


     
#Task_5

list_=[x/10 for x in range (10,31)]
print(list_)
           


     
#Task_6

hw_labels = []
list_=["Task_"+str(i) for i in range(14)]
print(list_)      


     
#Task_7

students = ['Answer_DZ_3-yudkevyc.v@gmail.com.ipynb',
            'Answer_DZ_3-eshmukhamedoa@gmail.com.ipynb',
            'Answer_DZ_3-amiimere@gmail.com.ipynb',
            'Answer_DZ_3-abin.saubanova@gmail.com.ipynb',
            'Answer_DZ_3-abyv56@gmail.com.ipynb',
            'Answer_DZ_3-selgizbaeva@gmail.com.ipynb',
            'Answer_DZ_3-irzaimovazhibek@gmail.com.ipynb',
            'Answer_DZ_3-jarida@gmail.com.ipynb',
            'Answer_DZ_3-naa.zhaparov@gmail.com.ipynb',
            'Answer_DZ_3-edrymanaliev4@gmail.com.ipynb',
            'Answer_DZ_3-ikn.akmatova@gmail.com.ipynb',
            'Answer_DZ_3-ekaeenalieva@gmail.com.ipynb',
            'Answer_DZ_3-ulanovaaziza313@mail.ru.ipynb',
            'Answer_DZ_3-umk.kg@gmail.com.ipynb',
            'Answer_DZ_3-lar.bojokoev@gmail.com.ipynb',
            'Answer_DZ_3-adshov.s@gmail.com.ipynb',
            'Answer_DZ_3-ndiakaidueva@gmail.com.py',
            'Answer_DZ_3-ultaovbekma@gmail.com.ipynb',
            'Answer_DZ_3-lexosankov@gmail.com.ipynb',
            'Answer_DZ_3-izarsesbaev@gmail.com.ipynb',
            'Answer_DZ_3-isuuu.lanbetova@gmail.com.ipynb']
gmails=[]
for s in students:
    if s.endswith('.ipynb'):
        email=s.split('-')[1].replace(".ipynb",'')
        gmails.append(email)
print(gmails)


     
#Task_8

list_ = [i for i in range(21) if i%2==0]
print(list_)
     


     
#Task_9

students = ['Answer_DZ_1-isuluu (1).kalmanbetova@gmail.com.ipynb',
            'Answer_DZ_1-isuluu.kalmanbetova@gmail.com.ipynb',
            'Answer_DZ_1-adyshov.s@gmail.com.ipynb',
            'Answer_DZ_3-yudkevych.v@gmail.com.ipynb',
            'Answer_DZ_1-selegizbaeva@gmail.com.ipynb',
            'Answer_DZ_2-adyshov.s@gmail.com.ipynb',
            'Answer_DZ_1-ekajeenalieva@gmail.com.ipynb',
            'Answer_DZ_1-abyev56@gmail.com.ipynb',
            'Answer_DZ_2-selegizbaeva@gmail.com.ipynb',
            'Answer_DZ_2-irzakimovazhibek@gmail.com.ipynb',
            'Answer_DZ_2-ldar.bojokoev@gmail.com.ipynb',
            'Answer_DZ_4-yudkevych (1).v@gmail.com.ipynb',
            'Answer_DZ_2-imonlobgromov@gmail.com.ipynb',
            'Answer_DZ_1-izaersesbaev@gmail.com.ipynb',
            'Answer_DZ_2-ekturamatov@gmail.com.ipynb',
            'Answer_DZ_2-amilimere@gmail (1).com.ipynb',
            'Answer_DZ_2-aimbekovakamila@gmail.com.ipynb',
            'Answer_DZ_2-nara.zhaparov@gmail.com.ipynb']
gmails=[]
for s in students:
    s.replace(".ipynb","")
    s.replace("Answer_DZ_","")
    email=s.split("-")[1]
    if email not in gmails:
        if '(1)' not in s:
            gmails.append(email)
print(gmails)


     
#Task_10

check_list = ['yes', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'yes']
result=[1 if x=='yes' else 0 for x in check_list]
print(result)
     
#Task_11

str_ ="Предприятие N, которое было запущено в 1976 году к 25 съезду КПСС, в этом году наростило выпуск готовой продукции на 20%. Из выпущенных холодильников, в этому году их количество на 100 едениц превысило выпуск прошлого года. Мы идем поставленным Партией курсом на увеличение мощностей по выпуску товаров народного потребления: в текущем году товары народного потребления составили 65% от всей производимой номенклатуры. Мы планируем наростить процент выпускаемой продукции на следующие 5 лет на 40%. Поставленные планы будут выполнены!"
numbers=[int(word) for word in str_.split() if word.isdigit()]
print(numbers)
     


   


     
#Task_12

import random
from random import randint
     

color_list = ['red', 'blue', 'green']
res_list = [color_list[random.randint(0,len(color_list)-1)] for _ in range(11)]
print(res_list)
     



     
#Task_13

import math
from math import *
from math import atan

katet_1 = [3, 5, 4, 6, 7, 9, 3, 4, 1, 5]
katet_2 = [6, 4, 5, 2, 7, 9, 1, 5, 4, 3]

hypotenuse=[(k1**2+k2**2)**0.5 for k1,k2 in zip(katet_1,katet_2)]
tan_min=[min(k1,k2)/max(k1,k2) for k1,k2 in zip(katet_1,katet_2)]
sin_min=[min(k1,k2)/h for k1,k2,h in zip(katet_1,katet_2,hypotenuse)]
min_angle=[math.degrees(atan(t)) for t in tan_min]
s_each=[k1*k2/2 for k1,k2 in zip(katet_1,katet_2)]
s_circle=[math.pi*(c/2)**2 for c in hypotenuse]

print("hypotenuse:", hypotenuse)
print("sin_min:", sin_min)
print("tan_min:", tan_min)
print("min_angle:", min_angle)
print("s_each:", s_each)
print("s_circle:", s_circle)

     
#Task_14

cw_1 = [2, 4, 4, 5, 3, 3, 5, 4, 2, 3]
cw_2 = [5, 4, 4, 3, 4, 3, 4, 5, 3, 5]
cw_3 = [3, 4, 4, 4, 5, 5, 4, 3, 3, 2]
     
import math
cw1_m=sum(cw_1)/len(cw_1)
cw2_m=sum(cw_2)/len(cw_2)
cw3_m=sum(cw_3)/len(cw_3)
if cw1_m<int(cw1_m)+0.7:
    print(int(cw1_m))
else:
    print(int(cw1_m)+1)

if cw2_m<int(cw2_m)+0.7:
    print(int(cw2_m))
else:
    print(int(cw2_m)+1)

if cw3_m<int(cw3_m)+0.7:
    print(int(cw3_m))
else:
    print(int(cw3_m)+1)


     
#Task_15

id_list = [23, 245, 3, 3245, 23456, 2, 12, 134, 43, 2311, 23, 95]
     
id_00000=['ID_'+('0000'+str(i))[-5:] for i in id_list]
print(id_00000) 


     
#Task_16

list_1 = ['a', 'b', 'c', 2, 4, 6, 8, 'f']
list_2 = [4, 6, 10, 13, 'b', 'c', 'g', 'r']
import math
list_=[i for i in list_1 if i in list_2]
print(list_)


     
#Task_17

list_ = [1, 3, 5, 4, 2, 6, 'a', 'b', 'c', 'd', 'q']
list_r = [i for idx, i in enumerate(list_) if idx % 2 == 0]
list_k = [i for idx, i in enumerate(list_) if idx % 2 == 1]
list_k.reverse()

list_r = sorted(list_r, key=str)
list_k = sorted(list_k, key=str, reverse=True)

result = []
r = k = 0

for i in range(len(list_)):
    if i % 2 == 0:
        result.append(list_r[r])
        r += 1
    else:
        result.append(list_k[k])
        k += 1

print(result)

     
#Task_18

list_ = [129, 200, -300, -28, 1, 123, -132, -53, 43, 200, 79, 193, -79]

list_norm=[(i-min(list_))/(max(list_)-min(list_)) for i in list_]
print(list_norm)


     


     
#Task_19*

list_ = [150, 149, 178, 170, 200, 198, 189, 161, 171, 164, 195, 186]

list_st=[(i-sum(list_)/len(list_))**2 for i in list_]
variance=(1/len(list_)*sum(list_st))
delta=variance**0.5
print(delta)