class NumberMachine:
    """
    A class that performs three operations on a number:
    1. Reverse the digits
    2. Calculate the sum of digits
    3. Increment each digit by 1 (with wrap-around for 9 -> 0)
    """

    def __init__(self, number: int):
        """
        Initialize the NumberMachine with a given number.

        :param number: Five-digit integer to process
        """
        self.number = number

    def reverse_number(self) -> int:
        """
        Reverse the digits of the number without using built-in reverse functions.

        :return: Reversed integer
        """
        n = self.number
        reversed_num = 0

        # Extract digits one by one using modulus and integer division
        while n > 0:
            digit = n % 10               # Get rightmost digit
            reversed_num = reversed_num * 10 + digit
            n //= 10                     # Remove rightmost digit

        return reversed_num

    def sum_of_digits(self) -> int:
        """
        Calculate the sum of all digits in the number.

        :return: Sum of digits
        """
        return sum(int(d) for d in str(self.number))

    def increment_digits(self) -> int:
        """
        Increment each digit by 1.
        If a digit is 9, it wraps around to 0.

        :return: New number with incremented digits
        """
        result = ""

        for d in str(self.number):
            # Add 1 to each digit and apply modulo 10 for wrap-around
            result += str((int(d) + 1) % 10)

        return int(result)


if __name__ == "__main__":
    # Example usage
    nm = NumberMachine(12391)

    print("Reversed:", nm.reverse_number())
    print("Digit sum:", nm.sum_of_digits())
    print("Incremented:", nm.increment_digits())
