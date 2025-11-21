from global_utils import ascii_lowercase

ciphertext = "ltctfd{p-peye-mp-raee-ieu}"
key = "tellmewhy"

solution = ""
for idx, char in enumerate(ciphertext):
    if char in ascii_lowercase:
        char_idx = ascii_lowercase.index(char)
        key_idx = ascii_lowercase.index(key[idx % len(key)])
        solution += ascii_lowercase[(char_idx - key_idx) % 26]
    else: solution += char

print(solution)
