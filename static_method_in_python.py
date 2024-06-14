class Book:
    class_variable= "Hello hello "
    # Attribute or property section 
    # In this section we define the state/property of the object 
    title= ""
    author= ""
    price= 0.0
    discount = 0.0 
    
    # COnstructer 
    def __init__(self,title , author_name , price ,discount_rate):
      
       # -------->Constructer is used for initialization of object properties
      self.author= author_name
      self.title= title
      self.price = price
      self.discount= discount_rate
      print("I am constructor of book class",self)


    @classmethod
    def create_object(cls,title, author_name,price,discount_rate):
       print("Inside class method ", cls.class_variable)
       return cls(title,author_name,price,discount_rate)
    
    @staticmethod
    def add_two_numbers(num1,num2):
       return num1+num2

    


    #    Behaviour or methods section 
    def calculate_sp(self):
        self.sp = self.price- (self.price*self.discount/100)
       

#calling static function 
        sum= Book.add_two_numbers(10,20)
        print (sum)
# Instantiating the class or creating an object of the class 

book1 = Book("Munamadan", "Laxmi prsasad Devkota", 200, 20)
book2= Book(title="JAVA" , author_name="JOHN", price=100,discount_rate=30)

# Accesing object attributes 
#  we can access object attributes and methods using dot operator 
# print(book1.title)

# print(book1.author)
# print(book1.price)
# print(book1.discount)

# # print(book1.class_variable)


# # print(book2.class_variable)

# book1.calculate_sp()
# print(f"The sp of book1 is: {book1.sp}")
# print(book2.title)
# print(book2.author)
# print(book2.price)
# print(book2.discount)

# book2.calculate_sp()
# print(f"SP of book2 is: {book2.sp}")

#calling class method 
book1 = Book.create_object("python","Ressum",1000,10)
print(book1.title)







