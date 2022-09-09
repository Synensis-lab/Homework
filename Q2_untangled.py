# This file is the Q2.py re-written in an effort (unsuccessfully)
# to be able to perform unit tests.

pin = '1234'
start_balance = 100

def get_pin():
    global usinput1
    usinput1 = input('Enter your 4 digit pin number with no spaces: ')
    compare_pin()


def compare_pin():
    if usinput1 == pin:
        pin_correct()
    if usinput1 != pin:
        pin_not_correct()

def pin_correct():
    print('Correct pin')
    withdrawal_request()


def pin_not_correct():
    global usinput2
    print('Pin not correct. Try again. You have three attempts')
    usinput2 = input('Second attempt: Enter your 4 digit pin number with no spaces: ')
    if usinput2 == pin:
        pin_correct()
    else:
        # usinput2 != pin
        pin_not_correct_2()


def pin_not_correct_2():
    global usinput3
    print('Wrong Pin, please try again')
    usinput3 = input('Final Attempt: Enter your 4 digit pin number with no spaces: ')
    if usinput3 == pin:
        pin_correct()
    else:
        # usinput3 != pin
        print('You have entered the pin incorrectly 3 times')


def withdrawal_request():
    global withdraw_amt
    withdraw_amt = input('Enter amount you would like to withdraw: £')
    display_balance()


def display_balance():
    current_balance = start_balance - int(withdraw_amt)
    if current_balance > 0:
        print('Withdrawal successful: Your balance is now: £{}'.format(current_balance))
    else:
        withdrawal_negative_error()


def withdrawal_negative_error():
    print("You do not have enough funds to withdraw this amount. Your current balance is £{}.".format(start_balance))


# The bit where the functions run


get_pin()


















#
#
#         print('Pin not correct. Try again')
#
# pin_input()
#
# # for number in range(3):
#     pin_input()


#
#     pin_input()
#
#
#     if pin_input == pin:
#         print('Correct pin')
#         break
#     else:
#         print('Pin not correct. Try again')
#         uinput = input('Enter your 4 digit pin number with no spaces: ')
#
# if uinput != pin:
#     print('You did not enter correct pin. Your three tries are up!')
#     exit()
#
# start_balance = 100
# withdraw = int(input('Enter withdrawal amount: £'))
# current_balance = start_balance - withdraw
#
# try:
#     assert current_balance > 0
# except AssertionError:
#     print("You do not have enough funds to withdraw this amount. Your current balance is £{}.".format(start_balance))
#
# else:
#     print('Your balance is now: £{}'.format(current_balance))