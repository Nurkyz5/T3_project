#==============Collections===========
#standart strycyre of data(list,dict,set,tuple)
#recovers several items

#though module collections represents wide box, which:
'''
1) eases codes
2) increases productivity
3) adds convenient abstractions
'''

#collection is the part of standart Python's library
#realizes special boxes which were optimized for concrete scenarios and problems

#Using data structure which is fully apllicable for problem
# data-oriented design


#import collections
from collections import Counter

#=============Counter============
#Counter is more than just counting
#it is a subclass of dict where:
'''
key is the element itself
value is its' quantity
'''

a=[1,2,3,1,2,4,3]
counts=Counter(a)
print(counts)

a=Counter([1,2,3,1,2,4,3])
b=Counter([2,3,4,5,4,2,4])
print("\na, ",a)
print("\nb ,",b)


# + -
#intersect |
#union

print("\na+b,",a+b)
print("\na-b,",a-b)
print("\na|b,",a|b)

c=Counter(a=2,b=-1)
print(list(c.elements()))

#=========Real cases=========
'''
analyzing logs
NLP(words)
'''


#============defaultdict============
#problems if standart dict
dict_1={}

from collections import defaultdict

#defaultdict(factory_function)

#ways to use:
'''
1) counter 
d=defaultdict(int)
'''
d=defaultdict(int)
'''list'''
d=defaultdict(list)
'''set'''
d=defaultdict(set)


a=defaultdict(int)
a["key1"]+=1
a["key2"]+=2
print(a)

#============deque==================
#========it is an effective que===========
        # list  deque
#append    O(1)   O(2)
#pop(0)    O(n)   O(1)

#extra opportunities

from collections import deque
dq=deque([1,2,3],maxlen=3)
dq.append(4)
print(dq)

dq.rotate()
print(dq)

#deque is safe for poliflow use

#real cases:
#cash


#===============namedtuple=======================
from collections import namedtuple
user=namedtuple("user",['name','age','role'])
print(user)

u=user(name="Aktan",age="20",role="admin")
print(u)
print(u.name)


#===============ordereddict=============
from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict["a"]=1
ordered_dict["b"]=2
print(ordered_dict)

ordered_dict.move_to_end("a")
print(ordered_dict)




#===============ChainMap===============
#it is a unoin of a few dictionaries
from collections import ChainMap
dict1={
    "a":1,
    "b":2
}
dict2={
    "c":1,
    "d":4
}

chain_map=ChainMap(dict1,dict2)
print(chain_map)
print(chain_map['a'])
print(chain_map['b'])

# real cases
# configurations
# viewable area

# counter-> подсчет частоты
# defaultdict-> values default
# deque-> ques
#namedtuple->structured recored
#ChainMap->union of dictionaries

#======================Practice======================
text="Hello my name is Aktan. i am 23 years old. I am learning Python"

#problem is to count words
from collections import Counter
words=text.lower().split(" ")
counter=Counter(words)
print(counter)

#Problem: реализовать очередь задач с добавлением в начало и конец
from collections import deque
queue=deque()
queue.append("task1")
queue.append("task")
print(queue)

print(queue.pop())
print(queue.popleft())


# Problem: to find 3 most numbers
list1=[1,1,1,2,2,3,3,3,5,5,4,4,4]
list_counter=Counter(list1)
print(list_counter.most_common(3))

#settings which are given defaultly and also are given bu user

default={"theme":"light","lang":"en"}
user={"lang":"ru",}
chain_map=ChainMap(default,user)
print(chain_map["lang"])



#task: divide into groups
students = [
    ('Alice', 1),
    ('Bob', 2),
    ('Charlie', 1)
]



groups=defaultdict(list)
for name,course in students:
    groups[course].append(name)
print(dict(groups))