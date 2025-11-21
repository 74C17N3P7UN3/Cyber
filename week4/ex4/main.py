from global_utils import hex_to_bytes, most_freq_char

with open("encrypted.txt") as file:
    contents = file.read()

text_bytes = hex_to_bytes(contents)

highest_freq = (0, 0)  # Tuple of type (key_len, dupes_count)
for key_len in range(6, 15):  # Step 1: Set the key length to test (6-14)
    # Step 2: Shift the string by key_len
    shifted_bytes = text_bytes[key_len:] + text_bytes[:key_len]
    # Step 3: Count the characters that are the same in the same position
    frequency = len([x for x, y in zip(text_bytes, shifted_bytes) if x == y])

    # Step 4: Take the highest frequency over different key lengths
    if frequency > highest_freq[1]:
        highest_freq = (key_len, frequency)

key_len = highest_freq[0]

# Cryptoanalysis
key_parts = [text_bytes[idx::key_len] for idx in range(key_len)]
most_freq_chars = [most_freq_char(key_parts[idx]) for idx in range(key_len)]

# We can assume " " as the most common decrypted character for every line
key = [char ^ ord(" ") for char in most_freq_chars]

decoded_text = ""
for idx, char in enumerate(text_bytes):
    decoded_text += chr(char ^ key[idx % key_len])

print(decoded_text.split("\n")[0])
