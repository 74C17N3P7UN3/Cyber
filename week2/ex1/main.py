numbers = [(1, 9, 4), (4, 2, 8), (4, 8, 3), (7, 1, 5), (8, 10, 1)]

with open("book.txt") as file:
    contents = file.read()

solution = ""
for position in numbers:
    paragraph = contents.split("\n\n")[position[0] - 1]
    line = paragraph.split("\n")[position[1] - 1]
    word = line.split(" ")[position[2] - 1]
    solution += word + " "
print(solution.strip())
