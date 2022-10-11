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

    def __init__(self, total_items):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    # This method asks user what part of the register they would like to use.
    def ask_user(self):
        while True:
            try:
                next_step = input("Cash Register Options = add, remove, show, discount, reset, end:  ").upper()
            except:
                print("Entry not recognised, try again")
                continue
            if next_step == "ADD" or next_step.startswith("A"):
                return CashRegister.add_item(self)
            elif next_step == "REMOVE":
                return CashRegister.remove_item(self)
            elif next_step == "SHOW":
                return CashRegister.show_items(self)
            elif next_step == "DISCOUNT" or next_step.startswith("D"):
                return CashRegister.apply_discount(self)
            elif next_step == "RESET":
                return CashRegister.reset_register(self)
            elif next_step == "END":
                print("Thank you")
                break
            else:
                quit()


    def add_item(self):
        total_items = {}
        while True:
            print("Enter the item and price")
            item_name = input("Item name: ").upper()
            try:
                item_price = round(float(input("Item price: £")), 2)
            except:
                print("Value not recognised, enter again")
                continue
            total_items[item_name] = item_price
            self.total_items.update(total_items)
            CashRegister.show_items(self)
            CashRegister.get_total(self)
            return CashRegister.ask_user(self)


    def remove_item(self):
        if self.total_items != None:
            item = True
            while True:
                item = input("State which item you would like to remove: ").upper()
                if self.total_items.get(item):
                    self.total_items.pop(item)
                    print("{} has been removed".format(item))
                    return CashRegister.ask_user(self)
                else:
                    print("input not understood please enter again")
                continue
        else:
            print("There are currently no items in the cash register! use the add option to enter items.")
            return CashRegister.ask_user(self)

    def apply_discount(self):
        while True:
            try:
                amount_discount = int(input("How much discount to be applied (percent): "))
            except:
                print("Value not understood, please re-enter percentage amount")
                return CashRegister.ask_user(self)
            print(amount_discount)
            self.discount = amount_discount
            percentage = 100 * (self.total_price/self.discount)
            print(percentage)
            print("Discount = £{}".format(percentage))
            return CashRegister.ask_user(self)

    def get_total(self):
        total = sum(self.total_items.values())
        print("Total cost: £{}".format(total))
        # return CashRegister.ask_user(self)

    def show_items(self):
        if len(self.total_items) > 0:
            print("Items: ")
            [print(key, "  ", value) for key, value in self.total_items.items()]
            return CashRegister.ask_user(self)
        else:
            print("There are currently no items in the cash register, use the add option to enter items")
            return CashRegister.ask_user(self)

        # if (self.total_items) != None:
        #     print("Your purchases are:")
        #     for key, value in self.total_items.items():
        #         return print(key, value)
        #

    def reset_register(self):
        pass


# create instance
bill_1 = CashRegister(None)
# EXAMPLE code run:
print(CashRegister.ask_user(bill_1))



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
