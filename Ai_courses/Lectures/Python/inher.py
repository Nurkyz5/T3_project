#============Abstraction and Mixins, they are little bit same===============
#======== it's 1 of 4(5) principes og OOP
# the role is hiding compound data and present to user only needed interface

#  why we need it:
#  contract - which methods must be realized in daughter's classes
# flexibilty - we can change realization not using code which is in abstraction
# masshtab - easy to add new realizations


#  основная роль абстракции - в том чтобы была правильность работы полиморфизма и наследования 

from abc import ABC, abstractmethod

#  чтобы класс или метод были абстрактными, надо класс унаследовать от ABC
#  а метод обернуть в декоратор abstractmethod


# class A(ABC):
#     @abstractmethod
#     def __init__(self):
#         pass

# class B(A):
#     pass

# b=B()

# print(b)
    
# пока не оборачиваем в декоратор...

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass #skip

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r
    
circle=Circle(5)
print(circle.area())
print(circle.perimeter())

# от абстрактного класса создавать объект нельзя



#  ============Миксины===========
#  This is class which gives definite functional for width of daughters' classes, bur it's not for self use

# It's merely the way of using the code again without hierarchy(heritance).

# Правила миксина:
# 1) Не должен иметь собственного __init__(или должен вызывать super().init())
# 2) it's not for creating экземпляров самостоятельно
# 3) Объект и экземпляр это одно и то же
# 3) Миксин добавляет ОДНУ конкретную возможность(для мотора мы создаем класс только мотор)
# 4) Название миксинов ДОЛЖНЫ заканчиваться на Mixin
# 5) Миксин идёт ПЕРЕД основными классами в списке наследования, ex: class Car(MotorMixin,ShinaMixin,Transport). Here Transport is the last.


class MotorMixin:
    # adds one concrete opportunity
    def start(self):
        print("Motor is runned")

class ShinaMixin:
    def krutitsa(self):
        print("Shinas krutyatsa")

class Transport:
    def __init__(self, brand):
        self.brand=brand
        
        
class Car(MotorMixin,ShinaMixin,Transport):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

car1=Car("Hunday",'Sonata')
car1.start()
car1.krutitsa()

class CreateMixin:
    def create(self):
        print("User is created")

class SaveMixin:
    def save(self):
        print("User is saved")

class User(CreateMixin,SaveMixin):
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

    def __str__(self):
        return f'{self.username}-----{self.email}'


user=User("Timatima",'12345',"tima@gmail.com")
print(user)
user.create()
user.save()





#=======Practice======

# class DiscountMixin:
    


# class LogerMixin:
#     print(f"The discount is {self.percent} for the price {self.price}")
# class Product(self,price,percent):
#     def __init__()
#     self.price=price
#     self.percent=percent
    


class DiscountMixin:
    def apply_discount(self, price, percent):
        return price - (price * percent / 100)


class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class Product(DiscountMixin, LoggerMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self, percent):
        new_price = self.apply_discount(self.price, percent)
        self.log(f"Применена скидка {percent}% к товару {self.name}")
        return new_price
    
product = Product("Redmi", 1000)

print(product.get_discounted_price(10))



class DiscountMixin:
    def apply_discount(self,price,percent):
        discount=price*percent/100
        return price-discount


class LogerMixin:
    def log(self,message):
        return f'[LOG]------{message}'
    
class Product(DiscountMixin,LogerMixin):

    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_disc(self, percent):
        self.percent=percent
    def __str__(self):
        return f'{self.name}'
product1=Product("Milk",45)
print(product1.apply_discount(product1.price,10))
print(product1.log("Вытащили скидку"))
