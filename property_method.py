# class Person:
#     def __init__(self,name,age): 
#         self._name = name
#         self._age=age

#     def get_name(self):
#         return self._name
#     def get_age(self):
#         return self._age
#     def set_name(self ,name):
#         self._name = name
#     def set_age(self,age):
#         self._age=age

# person1=Person("kismat", 21)
# print(person1.get_name())
# print(person1.get_age())

# person1.set_name("Hari")
# person1.set_age(22)

# print(f"New name and age are: {person1.get_name()} at age  {person1.get_age()}")

# ---------------------------------------------------------------------------
# Using @property decorator getter and setter methods 

class Student:
    def __init__(self,_name,_age):
        self._name= _name 
        self._age= _age 

    @property
    # Getter method for name 
    def name(self):
        print("Inside getter method for name")
        return self._name
    
    
    @property
    # Getter method for age 

    def age(self):
        print("Inside getter method for age ")
        return self._age
    
    @name.setter 
    def name(self,_name):
        self._name= _name 

    @age.setter
    def age(self,_age):
        self._age= _age


student1 = Student("Ram ",22)
print(student1._name)
print(student1._age)

student1.name = "hari"
student1.age = 30

print(student1.name)
print(student1.age)









        
