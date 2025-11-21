## Larry's encryption

To **decrypt** Larry's message, we have to basically do the encryption steps in **reverse**, knowing that he has
encrypted the message using `key = "Mu"`, and `R = 2` (which we will tackle later).

### Steps 1..4

First of all, **step 1** tells us that we have to use a plaintext that is **divisible by 12 bits**. \
We can get these blocks by splitting the ciphertext every 12th character like so:

```python
blocks = [ciphertext[idx:idx + 12] for idx in range(0, len(ciphertext), 12)]
```

Then, we have to reverse engineer the **block encryption loop**. Since **step 13** says to increment `r`, which is the
rotation number out of the total `R` rotations, we will have to do it in the **reverse order**. In code terms:

```python
for r in reversed(range(R)):
```

### Step 5

Divide the block into 2, 6bit sections `Lr` and `Rr`.

However, since we are doing it in the **reverse order**, **Step 12** tells us to `use Rr as Lr, and Rr_altered as Rr`.
So we can split the **block** into `Rr` and `Rr_alt` like so:

```python
def split_block(block: str) -> tuple[str, str]:
    half = len(block) // 2
    return block[:half], block[half:]

Rr, Rr_alt = split_block(block)
```

Great, we have `Rr`! However, to reconstruct the **original block** we need `Lr`. In order to retrieve its value, we
need to continue to follow the loop's instructions. After the previous **step 5**, we can proceed with:

### Step 6

Using `Rr`, "**expand**" the value from 6 bits to 8 bits like so: `1..6 -> 1 2 4 3 4 3 5 6`

```python
def expand_block(block: str) -> str:
    return block[0:2] + (block[3:1:-1] * 2) + block[4:6]

Rr_exp = expand_block(Rr)
```

### Step 7

**XOR** the result with 8 bits of the **Key** beginning with `Key[idx * R + r]`, where:

- `idx` is the current block's index
- `R` is the total rotations count
- `r` is the current rotation

```python
def bits_range(string: str, start: int, end: int) -> str:
    bits = ""
    for idx in range(start, end):
        bits += string[idx % len(string)]
    return bits

start = idx * R + r
key_range = bits_range(key_bin, start, start + 8)

Rr_xor = xor(Rr_exp, key_range)
```

### Steps 8, 9 & 10

**Divide** the result into 2, 4bit sections: `S1`, `S2`.

```python
S1, S2 = split_block(Rr_xor)
```

Then, calculate the 2, 3bit values using the two "**S-boxes**" below.
Since both `S1` and `S2` are **4 bits** long, the first bit represents the row
and the other 3 represent the column, in **base 2**.

| S1 | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0  | 101 | 010 | 001 | 110 | 011 | 100 | 111 | 000 |
| 1  | 001 | 100 | 110 | 010 | 000 | 111 | 101 | 011 |

| S2 | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0  | 100 | 000 | 110 | 101 | 111 | 001 | 011 | 010 |
| 1  | 101 | 011 | 000 | 111 | 110 | 010 | 001 | 100 |

We can achieve the **conversion** by saving the tables in a **dictionary**, and then selecting the cell.

```python
def box(box_idx: int, block: str) -> str:
    boxes = {
        1: [
            ["101", "010", "001", "110", "011", "100", "111", "000"],
            ["001", "100", "110", "010", "000", "111", "101", "011"]
        ],
        2: [
            ["100", "000", "110", "101", "111", "001", "011", "010"],
            ["101", "011", "000", "111", "110", "010", "001", "100"]
        ]
    }

    chosen_box = boxes[box_idx]
    row = int(block[0])
    column = int(block[1:], 2)
    return chosen_box[row][column]

S1_box, S2_box = box(1, S1), box(2, S2)
```

Lastly, concatenate the results of the **S-boxes** into 1, 6bit value.

```python
result = S1_box + S2_box
```

### Finally, get back `Lr`

**Step 11** tells us to **XOR** the result above with `Lr` to obtain `Rr_alt`. \
This translates to: `Lr ^ result = Rr_alt`, but thanks to the XOR property, this implies that:

```text
Rr_alt ^ result = Lr
```

### Recursive encryption

We can now replace the block with the decrypted one for the next decryption cycle like so:

```python
block = Lr + Rr
```

After the **loop** has done all its cycles, we can add the **final block** to the **decrypted blocks** and move on with
the next one. In the end, we just need to convert the **decrypted** binary into ASCII characters to reveal the
**message**: `MiN0n!`

So ultimately, as asked by the description, the **flag** is:

```text
Gigem{MiN0n!}
```
