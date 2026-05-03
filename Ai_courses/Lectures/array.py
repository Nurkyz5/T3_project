# ================arrays in python==========


"""
list [] - Упорядоченные изменяемые данные
tuple () - кортеж - Упорядоченная неизменяемая коллекция
set {} - множество - неупорядоченное
"""

# Tuple

t={'hello,1,2'} #this is a set and it is unordered коллекция уникальных элементов


# ==============list methods==============

l=[1,2,3,4,5]
k=l.pop(-1)
print(l) #[1, 2, 3, 4]
# if there is no index, then function will pop last element
print(k)

# sort() - method to sort

element_list=[10,1,26]
element_list.sort()
print(element_list)
elem=['l','a','g']
elem.sort()
print(elem)
el=[1,6,2,3]
el.sort(reverse=True)
print(el)
# list.reverse()
# el.reverse()
# print(el) #[3, 2, 6, 1]

# ==========Tuple===========

# difference from list
#   speed tuple > list
#   tuple is not changeable, list is changeable
#   data storage list > tuple


print(dir(tuple))
print(dir(list))

# ======Tuple methods=========
# count(elements)
# index(show element's index)



num=1,1,2,3,4,1,2,3,4
print(num.count(1))
print(num.index(1))



# ===============set===========

t={1,2,4,5,6,1,1,4,3}
print(t)

# Methods

# add()
t.add(10)
print(t)
t.add('hello')
print(t)
t.add((60,70,81))
print(t)

# remove()
t.remove(5)
print(t)

# discard()
t.discard(10)
print(t)

# pop()
t.pop()
print(t)
t.pop()
print(t)

# union()
a={99,1000,3}
print(t.union(a))
print(t.intersection(a))
print(t.difference(a))




# =================Practice===========
numbers=[1,2,2,3,4,4,5]

a={2,4,5,6}
b={3,5,3,4}

print(a.intersection(b))
print(a.difference(b))
print(a.union(b))












