from global_utils import *

with open("zero_one.txt") as file:
    contents = file.read()

# Convert from "ZERO", "ONE" to "0", "1"
binary_string = literal_to_binary_str(contents)
# Convert from binary to an ascii string
ascii_string = binary_to_ascii(binary_string)
# Decode the base64 string
decoded_string_bytes = base64_decode(ascii_string)
decoded_string = decoded_string_bytes.decode("ascii")
# Decode the final morse code string
solution = morse_to_ascii(decoded_string)
print(solution)
