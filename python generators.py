# an example of an iterator implemented in Python
print('==EXAMPLE OF AN INTERATOR==')
class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration

numbers = Even(10)

print(next(numbers))
print(next(numbers))
print(next(numbers))

# python generators
# A generator is simply a function but with slight modification. 
# In generator function, we use the yield keyword to get the next item of the iterator.
print('==PYTHON GENERATORS==')
def even_generator():
    n = 0
    
    n += 2
    yield n

    n += 2
    yield n
    
    n += 2
    yield n

numbers = even_generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))

# make this generator return even numbers till a certain max number
print('==GENERATOR WITH CERTAIN MAX NUMBER==')
def even_generator(max):
    n = 2
    
    while n <= max:
        yield n
        n += 2

numbers = even_generator(4)

print(next(numbers))
print(next(numbers))
print(next(numbers))

# infinite stream of data with generators
print('==INFINITE STREAM OF DATA WITH GENERATORS==')
def generate_fibonacci():
    n1 = 0
    yield n1
    
    n2 = 1
    yield n2
    
    while True:
        n1, n2 = n2, n1 + n2
        yield n2
        
seq = generate_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

# another example
print('==ANOTHER EXAMPLE==')
def generate_odd():
    n = 1
    while True:
        yield n
        n += 2

odd_generator = generate_odd()

for num in range(10):
    print(next(odd_generator))