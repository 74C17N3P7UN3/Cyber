from random import randrange, seed as set_random_seed

from global_utils import xor_bytes

with open("top_secret.txt", "rb") as file:
    contents = file.read()

msg_bytes, time_bytes = contents[:-18], contents[-18:]

# Retrieve the cur_time at encryption
cur_time = xor_bytes(bytes([0x88] * 18), time_bytes)

# Regenerate the key with the previous time
set_random_seed(cur_time)
key = bytes([randrange(256) for _ in msg_bytes])

msg_bytes = xor_bytes(msg_bytes, key)
print(msg_bytes.decode("ascii"))
