with open("encrypted.txt") as file:
    contents = file.read()

subs_dict = {
    "A": "L",
    "B": "S",
    "C": "R",
    "D": "O",
    "E": "E",
    "F": "A",
    "G": "D",
    "H": "B",
    "I": "G",
    "J": "P",
    "K": "I",
    "L": "H",
    "M": "N",
    "N": "T",
    "O": "O",
    "P": "Y",
    "Q": "M",
    "R": "R",
    "S": "V",
    "T": "U",
    "U": "E",
    "V": "W",
    "W": "F",
    "X": "C",
    "Y": "Y",
    "Z": "Z"
}

converted_str = ""
for character in contents:
    if character in subs_dict:
        converted_str += subs_dict[character]
    else: converted_str += character

solution: str = converted_str.split(" ")[-1]
print(solution.strip())
