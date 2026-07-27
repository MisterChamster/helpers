# ================= Math =================
# abs divmod float int pow round sum complex hex oct 
q, r = divmod(17, 5)
print(q)  # 3
print(r)  # 2

print(pow(2, 3, 5))   # (2 ** 3) % 5

print(round(3.14159))   # .5 values round to the nearest even number

z = complex(2, 3)
print(z)       # (2+3j)
print(z.real)  # 2.0
print(z.imag)  # 3.0

print(complex("4+5j"))  # (4+5j)

print(hex(16))   # 0x10
print(oct(8))    # 0o10
print(bin(5))    # 0b101


# ================= Booleans =================
# bool all any
# All returns True only if every item is truthy
# Any returns True if at least one item is truthy


# ================= Text =================
# ascii chr format ord print repr str

# ascii - function returns a readable version of any object.
# Replaces any non-ascii characters with escape characters
# å will be replaced with \xe5

# chr - returns the character for a Unicode code point
print(chr(65)) # A
print(chr(97)) # a

# format - formats a value according to a format specifier

# ord - returns the Unicode code point of a single character
print(ord("A"))   # 65

# print(*objects, sep=' ', end='\n', file=None, flush=False)
with open("out.txt", "w") as f:
    print("Saved text", file=f)

# repr - official string representation of an object, meant to be unambiguous

# str - readable string version of an object, meant for users


# ================= Type / object inspection =================
# callable hasattr isinstance issubclass type id hash

# callable - returns True if the object can be called like a function
print(callable(len))        # True
print(callable(42))         # False

# hasattr - returns True if an object has a given attribute
class Person:
    name = "Ana"
p = Person()
print(hasattr(p, "name"))      # True
print(hasattr(p, "age"))       # False
print(hasattr(42, "__str__"))  # True

# isinstance checks if object is an instance of a class
print(isinstance(5, str))            # False
print(isinstance(5, (int, float)))   # True

# issubclass - checks if class is a subclass of another class
class Animal:
    pass
class Dog(Animal):
    pass
print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False
print(issubclass(int, object))   # True

# type - returns the type of an object
print(type(5) is int)   # True

# id - returns the identity of an object (int)
x = 4
print(id(x))

# hash - returns a hash value for an object (can't be used in iterables)
print(hash("hello"))
print(hash("abc") == hash("abc"))   # True


# ================= Sequence / iteration =================
# iter next len list tuple set frozenset dict range slice enumerate reversed sorted zip map filter


# ================= Attribute / scope =================
# getattr setattr delattr dir globals locals vars help


# ================= Files =================
# input open


# ================= Execution / runtime =================
# compile eval exec breakpoint __import__
# compile() takes Python source code as text and turns it into a code object. 
# A code object is an internal, executable form of the code that Python can run later
# exec() executes it. And works for statements.
source = """
x = 10
y = 20
print(x + y)"""
code = compile(source, "<string>", "exec")
exec(code)

# eval - takes a string containing a Python expression, evaluates it, and returns the result
# Works for expressions, not statements!
print(eval("2 + 3"))           # 5
print(eval("len('hello')"))    # 5

# breakpoint - super cool for debugging, stops program and lets you inspect current state
# of program before moving further
def divide(a, b):
    breakpoint()
    return a / b
divide(10, 2)

# __import__() is the low-level built-in import function that Python uses 
# behind the scenes for import word
math_module = __import__("math")
print(math_module.sqrt(16))


# ================= OOP =================
# classmethod staticmethod property super object
# classmethod - receives class as argument. Good for alt contructors!
class Dog:
    def __init__(self, name):
        self.name = name
    @classmethod
    def from_string(cls, text):
        return cls(text)
d = Dog.from_string("Doge")
print(d.name)   # Doge

# staticmethod - belongs to class namespace, but gets no automatic first argument
class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(2, 3))   # 5

# property - lets a method be accessed like an attribute
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
p = Person("John", "Coltrane")
print(p.full_name)   # John Coltrane

# Super - returns a proxy object that lets you call methods from a parent class
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name)   # Buddy
print(d.breed)  # Labrador

# object - base class that all classes inherit from
class A:
    pass
print(issubclass(A, object))  # True


# ================= Binary data =================
# bytes bytearray memoryview
# bytes - immutable sequence of bytes
data = bytes([65, 66, 67])
print(data)        # b'ABC'
print(data[0])     # 65

# bytearray - mutable sequence of bytes
data = bytearray([65, 66, 67])
data[0] = 90
print(data)        # bytearray(b'ZBC')

# memoryview - aview into an existing bytes-like object without copying it
data = bytearray(b"hello")
view = memoryview(data)
view[0] = ord("H")
print(data)        # bytearray(b'Hello')
print(view.tobytes())  # b'Hello'


# ================= Async =================
# aiter anext
# aiter - gets an async iterator from an async iterable
# anext - gets the next item from an async iterator

