# -*- coding: utf-8 -*-

"""
This is a pure python implementation of Dynamic Programming solution to fibonacci sequence problem.
"""

class Fibonacci:

    def __init__(self, N=None):
        if N:
            N = int(N)
            self.fib_array = [0] * (N+ + 1)
            print(self.fib_array)
            self.fib_array[0] = 0
            self.fib_array[1] = 1
            for i in range(2, N + 1):
                self.fib_array[i] = self.fib_array[i - 1] + self.fib_array[i - 2]

        else:
            self.fib_array = [None] * (N + 1)

    def get(self, sequence_no = None):
        if sequence_no:
            if sequence_no < len(self.fib_array):
                return print(self.fib_array[:sequence_no])
            else:
                print("Out of bound")
        else:
            print("Please specify the  a value.")

if __name__ == '__main__':
    import sys

    print("\n******** Fibonacci Series Using Dynamic Programming ********\n")
    # For python2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_fuction = input

    print("\n Enter the upper limit for the fibonacci sequence:\n")
    try:
        N = eval(input_fuction())
        fib = Fibonacci(N)

        print("\n******** Enter different values to get the corresponding fibonacci sequence, enter any negative number to exit. ********\n")
        while True:
            print("Enter value: ", end = " ")
            try:
                i = eval(input_fuction())
                if i < 0 :
                    print("\n******** Good bye! ********\n")
                    break;
                fib.get(i)
            except NameError:
                print("\nInvalid input, Please try again.")
    except NameError as e:
        print("\n******** Invalid input, good bye!! ********\n")
