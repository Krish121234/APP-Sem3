# class ClassName:
#     def __init__(self, division, year):
#         self.division = division
#         self.year = year
# 
#     def print_details(self):
#         return f"Class Details:\nDivision: {self.division}\nYear: {self.year}."
#     
# 
# my_class= ClassName("SY3", 2)
# print(my_class.print_details())

class Number:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            print(num," is even")
        else:
            print(num," is odd")

number = Number()
number.check_even_odd(10)
