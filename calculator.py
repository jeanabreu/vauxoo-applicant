"""
This script will receive  a list of numbers and return the sum of them.
"""


class CalculatorClass(object):

    """
    Using a list, we will save the numbers to be added in the method
    """
    list = []
    sum_number = 0

    def sum(self):
        # The value entered in Variable "x" by the user, will be the size of
        # the list.
        x = int(raw_input("Size of the List: "))
        for i in range(x):
            # The user will type the numbers to sum
            self.list.append(int(raw_input("Type the number: ")))
        for i in self.list:
            self.sum_number += i
        print "\n Sum Total:", self.sum_number


# The "sum" method will show the result
obj = CalculatorClass()
obj.sum()