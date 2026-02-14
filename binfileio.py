# Example: save bytes to a file
data = bytes([65, 66, 67, 68])  # This is A, B, C, D in ASCII

with open("data.bin", "wb") as f:
    f.write(data)

with open("data.bin", "rb") as f:
    content = f.read()
print(content)       # b'ABCD'
print(list(content)) # [65, 66, 67, 68]

import struct

# Pack two integers (4 bytes each) into binary
data = struct.pack("ii", 123, 456)

with open("numbers.bin", "wb") as f:
    f.write(data)

# Read them back
with open("numbers.bin", "rb") as f:
    content = f.read()

num1, num2 = struct.unpack("ii", content)
print(num1, num2)  # 123 456

with open("numbers.bin", "rb") as f:
    content = f.read()
    print(len(content))

with open("numbers.bin", "wb") as f:
    l = []
    for i in range (5):
        l.append(int(input("Enter an integer\n")))
    l.reverse()
    f.write(bytes(l))

with open("numbers.bin", "rb") as f:
    #content = f.read()
    #print(list(content))  # Prints the list of integers as bytes
    f64 = f.read(64)
    print(f64.hex()) 
