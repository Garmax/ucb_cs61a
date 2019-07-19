
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder(x):
        nonlocal n
        n+=1
        return n+x-1
    return adder


def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    for index, elem in enumerate(lst):
        lst[index]=fn(elem)
        
def moon(f):
    sun=0
    moon=[sun]
    def run(x):
        nonlocal sun,moon
        def sun(k):
            return [k]
        y=f(x)
        moon.append(sun(y))
        return moon[0] and moon[1]
    return run

moon(lambda x:moon)(1)