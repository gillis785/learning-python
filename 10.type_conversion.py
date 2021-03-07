# Type Conversion
# Converting type of data types
# Convert int 100 to a str
print(str(100))
# check if 100 is a int or str using type
print(type(str(100)))

# convert back to int
print(type(int(str(100))))
# This is like doing
a = str(100)
b = int(a)
c = type(b)
print(c)