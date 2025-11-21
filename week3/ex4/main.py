from global_utils import ascii_to_binary, binary_to_ascii
from utils import *

ciphertext = "011001010010001010001100010110000001000110000101"
blocks = [ciphertext[idx:idx + 12] for idx in range(0, len(ciphertext), 12)]

key, rotations = "Mu", 2

solution = ""
# We can use the same order, since they are independent
for idx, block in enumerate(blocks):
    # But we have to invert the rotations to backtrace the semi-blocks
    for rotation in reversed(range(rotations)):
        Rr, Rr_alt = split_block(block)  # Step 12

        # We can't obtain the original Lr yet,
        # but we can do the previous steps

        Rr_exp = expand_block(Rr)  # Step 6

        key_start = idx * rotations + rotation
        key_range = bits_range(ascii_to_binary(key), key_start, key_start + 8)
        Rr_xor = xor(Rr_exp, key_range, 8)  # Step 7

        S1, S2 = split_block(Rr_xor)  # Step 8
        S1_box, S2_box = box(1, S1), box(2, S2)  # Step 9
        result = S1_box + S2_box  # Step 10

        # Now we can get Lr, using the XOR property A ^ B = C -> A ^ C = B
        # Where A is Rr_alt, B is Lr and C is the result

        Lr = xor(Rr_alt, result, 6)  # Step 11 (6 bits)
        block = Lr + Rr  # Replace the block for the next encryption iteration

    solution += block  # After every block cycle, add it to the solution

# Finally, convert the decrypted binary message into ASCII characters
print(binary_to_ascii(solution))
