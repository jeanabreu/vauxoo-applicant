"""
This script will receive  a list of numbers and return the sum of them.
"""


class CalculatorClass(object):
    """
    Using a list, we will save the numbers to be added in the method
    """
    list = []

    def sum(self, num_list):
        """
        Method to calculate the sum of a list
        """
        # The value entered in Variable "x" by the user, will be the size of
        # the list.
        num_list = 0
        for nbr in range(num_list):
            # The user will type the numbers to this sum
            self.list.append(int(raw_input("Type the number: ")))
        for nbr in self.list:
            num_list += nbr
        return num_list
