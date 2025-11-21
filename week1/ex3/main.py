from random import choice

from global_utils import ascii_alphanumeric

solution = ""
for _ in range(10):
    solution += choice(ascii_alphanumeric)
print(solution)
