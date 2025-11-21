with open("challenge.txt") as file:
    contents = file.read()

subs_dict = {
    "A": "h",
    "B": "v",
    "C": "w",
    "D": "s",
    "E": "o",
    "F": "b",
    "G": "j",
    "H": "a",
    "I": "I",
    "J": "J",
    "K": "m",
    "L": "e",
    "M": "p",
    "N": "y",
    "O": "n",
    "P": "r",
    "Q": "k",
    "R": "u",
    "S": "t",
    "T": "z",
    "U": "l",
    "V": "f",
    "W": "g",
    "X": "i",
    "Y": "d",
    "Z": "c"
}

converted_str = ""
for character in contents:
    if character in subs_dict:
        converted_str += subs_dict[character]
    else:
        converted_str += character

solution: str = converted_str.split(" ")[-1]
print(solution.strip())
