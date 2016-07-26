import unittest
from mathmagician import *
# Test integer
# Test prime
# Test fibonacci
# Test argument determines number of output
# Test verify output of each method
class test_math(unittest.TestCase):
    """ Test math.
    """
    def test_print_integers(self):
        math = Mathmagician()
        self.assertEqual([1,2,3,4,5], math.print_integers(5))

    def test_print_prime(self):
        math = Mathmagician()
        prime = math.print_prime(9)
        self.assertEqual([3,5,7,9], prime)

    def test_print_fibonacci(self):
        math = Mathmagician()
        fib = math.print_fibonacci(8)
        self.assertEqual([1,1,2,3,5,8,13,21], fib)



if __name__ == '__main__': 
    unittest.main()
