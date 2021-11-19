text = input("Enter a name to convert into ascii values:")

byte_array = bytearray(text, 'utf8')

ascii_values = []
byte_list = []

for character in text:
    ascii_values.append(ord(character))
print(ascii_values)

for byte in byte_array:
    binary = bin(byte)
    byte_list.append(binary)
print(byte_list)