import time

class Mathmagician:

    def __init__(self):
        self.number = 0

    def menu(self):

        print("1. integer")
        print("2. prime")
        print("3. fibonacci")
        print("4. quit")
        choice = input("Type 1,2,3, or 4 here...> ")


        if choice == "1":
          number_to_output = input("How many numbers? ")
          self.print_integers(number_to_output)


        if choice == "2":
          number_to_output = input("How many numbers? ")
          self.print_prime(number_to_output)

        if choice == "3":
          number_to_output = input("How many numbers? ")
          self.print_fibonacci(number_to_output)

        if choice != "4":
            self.menu()


    def print_integers(self, number_to_output):
        numberList = []
        for num in range(1, int(number_to_output) + 1):
            numberList.append(num)

        self.slow_printer(numberList)
        return numberList

    def print_prime(self, number_to_output):
        primeList = []
        for num in range(2, int(number_to_output) + 1):
            if num % 2 == 1:
                primeList.append(num)

        self.slow_printer(primeList)
        return primeList

    def print_fibonacci(self, number_to_output):
        fibonacciList = []
        fib, n = 0, 1
        for num in range(1, int(number_to_output) + 1):
            fib, n = n, fib + n 
            fibonacciList.append(fib)


        self.slow_printer(fibonacciList)
        return fibonacciList

    def slow_printer(self, printList):
        for i in printList:
            print(i)
            time.sleep(0.5)




if __name__ == '__main__':
    math = Mathmagician()
    math.menu()
