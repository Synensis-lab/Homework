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
        self.discount_percentage = 0
        self.discount = 0

    # The ask_user method asks user what part of the register they would like to use.
    def ask_user(self):
        while True:
            try:
                next_step = input("Cash Register Options = add, remove item, checkout, discount, zero, end: ").upper()
            except:
                print("Entry not recognised, try again")
                continue
            if next_step == "ADD" or next_step.startswith("A"):
                return CashRegister.add_item(self)
            elif next_step == "REMOVE" or next_step.startswith("R"):
                return CashRegister.remove_item(self)
            elif next_step == "CHECKOUT" or next_step.startswith("C"):
                return CashRegister.show_receipt(self)
            elif next_step == "DISCOUNT" or next_step.startswith("D"):
                return CashRegister.amount_discount(self)
            elif next_step == "ZERO" or next_step.startswith("Z"):
                return CashRegister.reset_register(self)
            elif next_step == "END" or next_step.startswith("E"):
                print("Thank you")
                quit()
            else:
                print("Entry not recognised, try again ......")
                continue

    # add_item is to add items with values to the register - (if time allows make dictkeys able to take multiple values)
    def add_item(self):
        total_items = {}
        while True:
            print("Enter the item and price")
            item_name = input("Item name: ").upper()
            try:
                item_price = float(input("Item price: £"))
            except:
                print("Value not recognised, enter again")
                continue
            formatted_price = float("{:.2f}".format(item_price))
            total_items[item_name] = formatted_price
            self.total_items.update(total_items)
            print(CashRegister.show_items(self))
            print(CashRegister.get_total(self))
            break
        return CashRegister.ask_user(self)

    def remove_item(self):
        if self.total_items != {}:
            count = 0
            while True:
                item = input("State which item you would like to remove: ").upper()
                if self.total_items.get(item):
                    self.total_items.pop(item)
                    print("{} has been removed".format(item))
                    return CashRegister.ask_user(self)
                elif count < 3:
                    print("input not understood, re-enter item to remove")
                    count += 1
                    continue
                else:
                    print("Error! Invalid inputs. Please select from cash register options")
                    CashRegister.ask_user(self)
        else:
            print("There are currently no items in the cash register! use the add option to enter items.")
            return CashRegister.ask_user(self)

    def amount_discount(self):
        try:
            self.discount_percentage = float(input("How much discount to be applied (percent): "))
        except:
            print("Value not understood, please re-enter percentage amount")
            count = 1
            while count < 3:
                try:
                    self.discount_percentage = float(input("How much discount to be applied (percent): "))
                    break
                except:
                    count += 1
                    continue
            print("Error! Invalid inputs")
            CashRegister.ask_user(self)
        print("{} % will be calculated at checkout".format(self.discount_percentage))
        percentage_check = input("is this correct? yes or no?:  ").upper()
        if percentage_check == "YES" or percentage_check.startswith("Y"):
            print("Discount {}% confirmed".format(self.discount_percentage))
            CashRegister.ask_user(self)
        elif percentage_check == "NO" or percentage_check.startswith("N"):
            print("Choose discount from options and re-enter value")
            CashRegister.ask_user(self)
        return CashRegister.ask_user(self)

    def get_total(self):
        total = sum(self.total_items.values())
        self.total_price = float(total)
        return "Sub Total: £{}".format(total)
        # return CashRegister.ask_user(self)

    def apply_discount(self):
        if self.discount_percentage > 0:
            print("Customer Discount  =  {}%".format(self.discount_percentage))
            discount_amount = (self.total_price / 100) * self.discount_percentage
            self.discount = round(discount_amount, 2)
            print("Amount to deduct: £{}".format(self.discount))
            discount_total = float(self.total_price - self.discount)
            print("TOTAL (with discount): £{}".format(discount_total))
            return "Thanks!"
        else:
            print("No Discount")
            print("TOTAL: £{}".format(self.total_price))

    def show_items(self):
        if len(self.total_items) > 0:
            print("Items:")
            [print(key, "  ", value) for key, value in self.total_items.items()]
            return " "
        else:
            print("There are currently no items in the cash register, use the add option to enter items")
            return CashRegister.ask_user(self)

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0
        print("Cash Register Now Reset, choose and option")
        return CashRegister.ask_user(self)

    def show_receipt(self):
        CashRegister.date_time(self)
        CashRegister.show_items(self)
        print("Sub total: £{}".format(self.total_price))
        CashRegister.apply_discount(self)
        return "Thank you!"

    def vat_rate(self):
        pass

    def vat_calculate(self):
        pass

    def date_time(self):
        import datetime
        datetime_object = datetime.datetime.now()
        print(datetime_object)

    def transaction_number(self):
        pass

# create instance
bill_1 = CashRegister(None)
# EXAMPLE code run:
# To run the cash register use the ask_user method.

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
