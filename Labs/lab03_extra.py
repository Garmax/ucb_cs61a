""" Optional problems for Lab 3 """
import math

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return False
    else:
        ub=int(math.sqrt(n))
        i=3
        while i<=ub:
            if n%i==0:
                return False
            i+=2
        return True


    

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a<b:
        return gcd(b,a)
    else:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"

    def count_digits(n,digit):
        if n<10:
            if n==digit: return 1
            else: return 0
        else:
            return count_digits(n%10,digit)+count_digits(n//10,digit)

    if n<10:
        return 0
    else:
        return count_digits(n//10,10-n%10)+ten_pairs(n//10)