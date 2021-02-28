# bin() and complex
# int and float stored into memory which is binary
# b - Binary, x - Hex, o - Octal, d - Decimal
# bin() converts to binary 
print(complex(29)) # complex numbers and math
# convert to binary
print(bin(5)) # converts 5 to binary 
# python way of showing its binary 0b 5 = 101
print(bin(202)) # 0b 11001010

# remove the 0b from answer and add 8 bits
print (format(5, 'b').zfill(8))
# or
print (bin(30)[2:].zfill(8))
# or
print(format(202, '08b'))

# convert binary to decimal

print (int('0b101', 2)) # = 5
print (int('0b11001010', 2)) # = 202
# you can also remove the 0b, it will equal the same
print (int('11001010', 2))
# or
print (format(0b11001010, 'd'))


