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
        """
        Method to calculate the sum of a list
        """
        # The value entered in Variable "x" by the user, will be the size of
        # the list.
        list_input = int(raw_input("Size of the List: "))
        for nbr in range(list_input):
            # The user will type the numbers to sum
            self.list.append(int(raw_input("Type the number: ")))
        for nbr in self.list:
            self.sum_number += nbr
        print "\n Sum Total:", self.sum_number


# The "sum" method will show the result
# pylint: disable=C0103
calc = CalculatorClass()
calc.sum()
