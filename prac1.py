# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# 
#     def increment_price(self, amount):
#         self.price = self.price+amount
# 
#     def decrement_price(self, amount):
#         self.price = self.price - amount
# 
# car1 = Car("Toyota", 1000000)
# car2 = Car("Audi", 2130000)
# 
# car1.increment_price(50000)
# car2.decrement_price(65000)
# 
# print(car1.brand, car1.price)
# print(car2.brand, car2.price)


#File Handling

# with open("prac2.py", "a") as file:
#     file.write("\n#Hallo everynyan")
# with open("prac2.py", "r") as file:
#     content = file.read()
#     print(content)

#Exception Handling

# try:
#     num = int(input("Enter a number: "))
#     result = 100/num
#     print(f"Result = {result}")
# except ZeroDivisionError:
#     print("Cannot be divided by zero!")
# except ValueError:
#     print("Please enter a valid input!")
# except Exception as e:
#     print(f"An error occured: {e}")
# finally:
#     print("This always runs, error or not")


#Magic Methods
# class Car:
#     def __init__(self, Brand, Price):
#         self.Brand = Brand
#         self.Price = Price
#     def __str__(self):
#         return f"Details:\n{self.Brand}\n{self.Price}"
# 
#     def __add__(self, other):
#         return Car(f"{self.Brand}+{other.Brand}", self.Price + other.Price)
# 
#     def __len__(self):
#         return len(self.Price)
#     
# 
# car1 = Car("Toyota", 2500000)
# car2 = Car("Audi", 3500000)
# print(car1)
# print(car2)
# 
# car3 = car1 + car2
# print(car3)
# 
# print(len(car3))

