class Recursive_problems:
    """
    Question : 1 Write a recursive function to print first N natural numbers.
    Question : 2 Write a recursive function to print first N natural numbers in reverse order.
    Question : 3 Write a recursive function to print first N odd natural numbers.
    Question : 4 Write a recursive function to print first N even natural numbers.
    Question : 5 Write a recursive function to print first N odd natural numbers in reverse order.
    Question : 6 Write a recursive function to print first N even natural numbers in reverse order. 
    """

    def question_1(self, n):
        """ Write a recursive function to print first N natural numbers. """
        if n == 1:
            return 1
        print(self.question_1(n-1))
        return n
                
    def question_2(self, n):
        """Write a recursive function to print first N natural numbers in reverse order."""
        print(n)
        if n == 1:
            return
        self.question_2(n-1)

    def question_3(self, n):
        """Write a recursive function to print first N odd natural numbers."""
        if n == 1:
            return 1
        value = self.question_3(n - 1)
        print(value) if value % 2 != 0 else None
        return n

    def question_4(self, n):
        """Write a recursive function to print first N even natural numbers."""
        if n == 1:
            return 1
        value = self.question_4(n - 1)
        print(value) if value % 2 == 0 else None
        return n

    def question_5(self, n):
        """Write a recursive function to print first N odd natural numbers in reverse order."""
        print(n) if n % 2 != 0 else None
        if n == 1:
            return 1
        self.question_5(n - 1)

    def question_6(self, n):
        """Write a recursive function to print first N even natural numbers in reverse order."""
        print(n) if n % 2 == 0 else None
        if n == 1:
            return 1
        self.question_6(n - 1)
        

obj = Recursive_problems()
print(obj.__dir__())