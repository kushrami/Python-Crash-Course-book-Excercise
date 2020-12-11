#testcase for Excercise 11.3

import unittest 
import Excercise_11_3 as module

class EmployeeTest(unittest.TestCase):

    def test_give_default_raise(self):
        employee1 = module.Employee('tony','stark',10000)
        employee1.give_raise()
        self.assertEqual(15000,employee1.annualsalary) 
    def test_give_custom_raise(self):
        employee2 = module.Employee('thor','son of odin',10000)
        employee2.give_raise(5000)
        self.assertEqual(20000,employee2.annualsalary)

unittest.main()