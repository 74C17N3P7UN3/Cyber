from random import randrange, seed as set_random_seed
from time import time

cur_time = str(time()).encode("ascii")
set_random_seed(cur_time)

msg = input("Your message: ").encode("ascii")
key = [randrange(256) for _ in msg]
c = [m ^ k for m, k in zip(msg + cur_time, key + [0x88] * 18)]

with open("secret.txt", "wb") as f:
    f.write(bytes(c))
