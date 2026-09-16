# ============ Python Format Specifiers ============
# Alignment
print(f"{'hi':<6}")    # 'hi    '
print(f"{'hi':>6}")    # '    hi'
print(f"{'hi':^6}")    # '  hi  '
print(f"{-42:=6}")     # '-   42'

# Fill
print(f"{'hi':*<6}")   # 'hi****'
print(f"{'hi':*>6}")   # '****hi'
print(f"{'hi':*^6}")   # '**hi**'

# Sign
print(f"{42:+}")       # '+42'
print(f"{42:-}")       # '42'
print(f"{42: }")       # ' 42'

# Alternate form
print(f"{255:#x}")     # '0xff'
print(f"{255:#X}")     # '0XFF'
print(f"{255:#b}")     # '0b11111111'
print(f"{255:#o}")     # '0o377'

# Zero padding / width
print(f"{42:05}")      # '00042'
print(f"{42:8}")       # '      42'
print(f"{-42:05}")     # '-0042'
print(f"{42:08}")      # '00000042'

# Grouping
print(f"{1234567:,}")  # '1,234,567'
print(f"{1234567:_}")  # '1_234_567'
print(f"{1234567:n}")  # locale-dependent

# Precision
print(f"{3.14159:.2f}")  # '3.14'
print(f"{3.14159:.4f}")  # '3.1416'
print(f"{3.14159:.2g}")  # '3.1'
print(f"{'abcdef':.3}")  # 'abc'

# Number types
print(f"{42:d}")       # '42'
print(f"{42:b}")       # '101010'
print(f"{42:o}")       # '52'
print(f"{42:x}")       # '2a'
print(f"{42:X}")       # '2A'
print(f"{65:c}")       # 'A'

# Float types
print(f"{1234.5:e}")   # '1.234500e+03'
print(f"{1234.5:E}")   # '1.234500E+03'
print(f"{3.14:f}")     # '3.140000'
print(f"{3.14:F}")     # '3.140000'
print(f"{1234.5:g}")   # '1234.5'
print(f"{1234.5:G}")   # '1234.5'
print(f"{0.25:%}")     # '25.000000%'

# Strings
print(f"{'hello':s}")   # 'hello'
print(f"{'hello':>10}")  # '     hello'
print(f"{'hello':.3}")   # 'hel'

# Common combos
print(f"{42:08d}")        # '00000042'
print(f"{42:+8d}")        # '     +42'
print(f"{42:#06x}")       # '0x002a'
print(f"{1234567:,}")     # '1,234,567'
print(f"{3.14159:10.2f}") # '      3.14'
print(f"{'hi':*^10}")     # '****hi****'

name = "Alice"
age = 18
print("Name:", name, "Age:", age)
print("2026", "09", "16", sep="-")
print("Hello", end=" ")
