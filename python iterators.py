# python iterables
numbers = [1, 4, 9]
print(dir(numbers))

# We can see that there is a special __iter__() method among all these methods.
numbers = [1, 4, 9]

value = numbers.__iter__()
print(value)


# the next method()
numbers = [1, 4, 9]
value = numbers.__iter__()

item1 = value.__next__()
print(item1)


# working of for loops
num_list = [1, 4, 9]

iter_obj = iter(num_list)

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break

# The above code is equivalent to:
num_list = [1, 4, 9]

for element in num_list:
    print(element)


# creating custom iterators
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

