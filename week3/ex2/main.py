from global_utils import ascii_lowercase

ciphertext = "vhixoieemksktorywzvhxzijqni"
key = "caesar"  # Because it's the hint

solution = ""
for idx, char in enumerate(ciphertext):
    char_idx = ascii_lowercase.index(char)
    key_idx = ascii_lowercase.index(key[idx % len(key)])
    solution += ascii_lowercase[(char_idx - key_idx) % 26]
print(solution)
