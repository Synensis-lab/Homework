"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self):
        more_entries = "YES"
        total_items = {}
        while more_entries == "YES":
            print("Enter the item and price")
            item_name = input("Item name: ")
            item_price = round(float(input("Item price: £")), 2)
            total_items[item_name] = item_price
            print("Would you like to enter another item?")
            more_entries = input("yes or no?: ").upper()
        return "Thanks!"



    def remove_item(self):
        pass

    def apply_discount(self):
        amount_discount = int(input("How much discount to be applied (percent): "))
        print(amount_discount)



    def get_total(self):
        pass

    def show_items(self):
        pass

    def reset_register(self):
        pass


# create instance
Test_1 = CashRegister()
print(CashRegister.apply_discount(Test_1))
# EXAMPLE code run:

# ADD


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""

#
# class Student:
#
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
