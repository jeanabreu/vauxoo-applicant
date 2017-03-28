"""
This script will receive an integer and return if it is prime or NOT
"""


class PrimeClass(object):

    """
    We created a variable to capture the integer number
    """
    input_n = raw_input("Type a Number: ")
    
    def is_prime(self, num_int):
        """
        Method to calculate if a number is prime or NOT
        """
        # A loop is initialized to calculate the given number.
        num_int = int(input_n)
        counter = 0
        for nbr in range(1, self.num_int + 1):
            if (self.num_int % nbr) == 0:
                counter = counter + 1
            if counter >= 3:
                break
        # With the results, we show if the number is prime or NOT in a
        # comparison with val_bool variable
        val_bool = counter
        if val_bool == 2:
            return True
        else:
            return False
            