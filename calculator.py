"""
Resolution to problem py2:
This script will receive as input a list of numbers and
That output returns the sum of them.
"""


class calculator_class:
    # Using a list, we will save the numbers to be added in the method
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
obj = calculator_class()
obj.sum()
