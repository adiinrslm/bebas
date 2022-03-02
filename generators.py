# Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over

# execution of generators function
print("==GENERATORS FUNCTION==")
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

#   ///////////////////////
# /// print(next(cd))  //// 
#    /////////////////

# you can iterate over a generator object with a for in loop
print("\n==ITERATE GENERATORS WITH FOR LOOP==")
cd = countdown(3)
for x in cd:
    print(x)


# you can use it for functions that take iterables as input
print("\n==USE ITERABLES FUNCTION AS INPUT==")
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)

# the generators can save memory
# with a generator, no additional sequence is needed to store the numbers
# without a generator, the complete sequence has to be stored here in a list
print("\n========")
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")
# this is how generators save the memory
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")


# example with fibonacci numbers
print("\n==FIBONACCI NUMBERS==")
def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))

# generators expressions
# generators can be written in the same syntax except with parenthesis instead of square brackets
print("\n==GENERATOS EXPRESSIONS==")
# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))

# concept behind generators
# It has to implement __iter__ and __next__ to make it iterable
print("\n==THE GENERATORS CONCEPT==")
class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()
             
firstn_object = firstn(1000000)
print(sum(firstn_object))