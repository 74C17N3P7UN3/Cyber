from global_utils import binary_to_ascii, literal_to_binary_str

with open("challenge.txt") as file:
    contents = file.read()

binary_string = ""
for character in contents:
    if character.isupper():
        binary_string += character

binary_bits = literal_to_binary_str(binary_string)
solution = binary_to_ascii(binary_bits)
print(solution)
