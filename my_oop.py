# class Cars:
#     def __init__(self, name, color, speed):
#        self.name = name
#        self.color = color
#        self.speed = speed

#     def set_color(self, value):
#         self.color = value

#     def get_color(self)                                                               




# class Student:

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


# class Computer: ##### Computer is the class name #######
#     def config(self):
#         print("15, 16gb, 1tn")
# com1 = Computer()   ### # com1 is the object#####
# com2 = Computer()
# print(type(com1)) 

# Computer.config(com1) #### com1 is been passed as an argument#####
# Computer.config(com1)

##############################

# class Student:
#     def scores(self):
#         print("27, 56, 89")
# English = Student
# maths = Student
# igbo = Student
# print(type(English))
# Student.scores(English)    


# class Computer:

#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

#     def config(self):
#         print(f"Your CPU spec is {self.cpu} and your RAM is {self.ram}") ##### self is used to fetch out the value

# com1 = Computer("i5", 16)   ####i5 and 16 are the object#####  com1 is the variable
# com2 = Computer("Ryzen 3", 8)

# com1.config()
# com2.config()

#########OOP 


# class Student:
#     def __init__(self, maths, physics,):
#         self.maths = maths
#         self.physics = physics

#     def scores(self):
#         print(f"scores for Maths is  {self.maths} and the score for physics is {self.physics}")
# Ma = Student(47, 834)
# ph= Student(57, 89)

# Ma.scores()
# ph.scores()



# class Student:
#     def __init__(self, maths, physics,):
#         self.maths = maths
#         self.physics = physics

#     def scores(self):
#         print( self.maths} and the score for physics is {self.physics}")
# Ma = Student(47, 834)
# ph= Student(57, 89)

# Ma.scores()
# ph.scores()













# class Product:
#     def __init__ (self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def _str_(self):
#         return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"


# class Inventory:
#     def __init__(self):
#         self.products = {}

#     def add_product(self):
#         print("\n=== Add New Product ===")
#         name = input("Enter product name: ")
        
#         # Input validation for price
#         while True:
#             try:
#                 price = float(input("Enter price: $"))
#                 if price >= 0:
#                     break
#                 print("Price cannot be negative!")
#             except ValueError:
#                 print("Please enter a valid number!")
        
#         # Input validation for quantity
#         while True:
#             try:
#                 quantity = int(input("Enter quantity: "))
#                 if quantity >= 0:
#                     break
#                 print("Quantity cannot be negative!")
#             except ValueError:
#                 print("Please enter a valid number!")

#         self.products[name] = Product(name, price, quantity)
#         print(f"\n{name} has been added to inventory!")

#     def update_quantity(self):
#         print("\n=== Update Product Quantity ===")
#         self.show_products()
#         name = input("Enter product name to update: ")
        
#         if name in self.products:
#             while True:
#                 try:
#                     new_quantity = int(input("Enter new quantity: "))
#                     if new_quantity >= 0:
#                         self.products[name].quantity = new_quantity
#                         print(f"\nQuantity updated for {name}!")
#                         break
#                     print("Quantity cannot be negative!")
#                 except ValueError:
#                     print("Please enter a valid number!")
#         else:
#             print("Product not found!")

#     def update_price(self):
#         print("\n=== Update Product Price ===")
#         self.show_products()
#         name = input("Enter product name to update: ")
        
#         if name in self.products:
#             while True:
#                 try:
#                     new_price = float(input("Enter new price: $"))
#                     if new_price >= 0:
#                         self.products[name].price = new_price
#                         print(f"\nPrice updated for {name}!")
#                         break
#                     print("Price cannot be negative!")
#                 except ValueError:
#                     print("Please enter a valid number!")
#         else:
#             print("Product not found!")

#     def remove_product(self):
#         print("\n=== Remove Product ===")
#         self.show_products()
#         name = input("Enter product name to remove: ")
        
#         if name in self.products:
#             del self.products[name]
#             print(f"\n{name} has been removed from inventory!")
#         else:
#             print("Product not found!")

#     def show_products(self):
#         if not self.products:
#             print("\nInventory is empty!")
#             return
        
#         print("\n=== Current Inventory ===")
#         for product in self.products.values():
#             print(product)

#     def show_total_value(self):
#         total = sum(product.price * product.quantity for product in self.products.values())
#         print(f"\nTotal Inventory Value: ${total:.2f}")


# def main():
#     inventory = Inventory()
    
#     while True:
#         print("\n=== Inventory Management System ===")
#         print("1. Add new product")
#         print("2. Update quantity")
#         print("3. Update price")
#         print("4. Remove product")
#         print("5. Show all products")
#         print("6. Show total inventory value")
#         print("7. Exit")
        
#         choice = input("\nEnter your choice (1-7): ")
        
#         if choice == '1':
#             inventory.add_product()
#         elif choice == '2':
#             inventory.update_quantity()
#         elif choice == '3':
#             inventory.update_price()
#         elif choice == '4':
#             inventory.remove_product()
#         elif choice == '5':
#             inventory.show_products()
#         elif choice == '6':
#             inventory.show_total_value()
#         elif choice == '7':
#             print("\nThank you for using the Inventory Management System!")
#             break
#         else:
#             print("\nInvalid choice! Please try again.")


# if __name__ == "__main__":
#     main()


# class Dog:
#     def bark(self):
#         return "Woof!"

# my_dog = Dog()  # my_dog is an object of class Dog
# print(my_dog.bark())  # Output: Woof!






# class Student:
#     def scores(self):
#         return"smart!"
# ada = Student()
# print(ada.scores())

