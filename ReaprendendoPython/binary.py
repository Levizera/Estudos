a_string = input("Insira uma Palavra: ")
a_byte_array = bytearray(a_string, "utf8")
#Create bytearray
byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    #Convert to binary
    byte_list.append(binary_representation)
    #Add to list

print(byte_list)
