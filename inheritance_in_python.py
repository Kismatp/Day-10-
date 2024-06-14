class Person:
    def __init__(self,name,age,address): 
        self.name = name
        self.age= age
        self.address= address
    def display_info(self):
        print("I am displaying person info: ")
        print("Name :",self.name)
        print("Age: ",self.age)
        print("Address: ", self.address)
    def person_method(self):
        print("I am a person and i can work  ")

class Student(Person):
    def __init__(self, name, age, address, university ):
        super().__init__(name,age,address)
        self.university= university

    # Person class has same method display_info() , so this will overridethat method 
    # to call the overrided method, 
    def display_info(self):
        print("I am displaying student's info: ")
        # print("Name :",self.name)
        # print("Age: ",self.age)
        # print("Address: ", self.address)
        print("University: ",self.university)

    def student_method(self):
        print("I am a student i can study ")

# Creating object of sub class i.e. Students 
Student1= Student("hari",25,"bharatpur","khwopa ")
print(Student1.display_info())
Student1.student_method()
Student1.person_method()



# Student2= Student("Kismat", 21,"CHitwan", "Tribhuwan University")
# print(Student2.display_info())

# person1=Person("RAM", 21,"bhaktapur" )
# print(person1.display_info())




   