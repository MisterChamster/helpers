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


# ================= OOP =================
# classmethod staticmethod property super object


# ================= Binary data =================
# bytes bytearray memoryview


# ================= Async =================
# aiter anext


