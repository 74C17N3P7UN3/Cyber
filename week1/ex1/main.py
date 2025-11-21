from global_utils import ascii_lowercase

string = "abcde"
shift_amount = 2

solution = ""
for character in string:
    char_idx = ascii_lowercase.index(character)
    shifted_idx = (char_idx + shift_amount) % 26
    solution += ascii_lowercase[shifted_idx]
print(solution)
