#  HELP! I am really stuck on this - I have written notes to try to explain what I am trying
# to do but have failed to be able to do this!!!!


# First I rewrote the code from Q2.py to chunk it all into functions this is found in Q2_untangled file

# The classes of unit tests I would like to run are:
# Tests 1. Check the user input is processed correctly in get_pin
# Tests 2. Check pin_code_correct is functioning
# Tests 3. Check pin_not_correct is functioning
# Tests 4. Check withdrawal_request takes input
# Tests 5. Check display_balance if and else options


# Tests 1 - Check: when user input is received the function compare_pin is executed
# I think I need to use mock and patch, but I am totally stuck with this - this type
# of test is also needed for Tests 4.

# from unittest import mock
# from unittest import TestCase, main
# from Q2_untangled import get_pin
#     @mock.patch(Q2_untangled.usinput1)
#     def checkComparePinCalled(self, mock_usinput):
#         content = []
#         expected = compare_pin()
#         self.assertTrue(expected, result)


# Tests 2 - Check pin_code_correct is functioning.
# This class of tests checks:
# 2.1 Check that when variable usinput1 equals pin then pin_correct function runs
# 2.2 Check if variable usinput1 is  mot the same as pin then pin_not_correct function runs

from unittest import TestCase, main
from Q2_untangled import compare_pin


class test_Compare_Pin(TestCase):
    def pin_correct(self):
        result = 1234
        expected = 0
        self.assertEqual(expected, result)

    def pin_not_correct(self):
        result = 2345
        expected = 1
        self.assertEqual(expected, result)

# Test 3. Check pin_not_correct is functioning
# This class of tests checks that
# 3.1. check function asks user for  input
# 3.2. if user input = pin then pin_correct function runs
# 3.3. if user input != pin then function pin_not_correct_2 runs


# Test 4. Check withdrawal_request takes input
# This class of tests checks:
# when receive withdraw_amt variable is received  from user then display_balance function runs
# (this is the same test as test 1 which i think uses mock and patch)

# Test 5. Check display_balance if and else options
# This class of tests checks:
# 5.1 the variable current_balance is calculated correctly
# 5.2 check for current_balance being positive integer
# 5.3 check for current_balance being negative integer
# 5.4 check for current_balance being float
# 5.5 check for current_balance being another data type



from unittest import TestCase, main
from Q2_untangled import pin_not_correct



# class test_compare_pin(TestCase):
#     def pin_good(self):
#         result = '1234'
#         expected =
#
#
# class test_calculate_balance(TestCase):
#     def calculate_balance(self):
#         pass
#
# class test_display_balance(TestCase):
#     def display_balance(self):
#         pass
#
# class test_withrawal_negative_error:
#     def withdrawal_negative_error(self):
#         pass
#
#
