## Repeated XOR

As specified in the description, the encrypted text is **hex-encoded**.
So, we can start by converting it into **bytes**.

```python
def hex_to_bytes(hex_str: str) -> bytes:
    return (int(hex_str, 16)
            .to_bytes(len(hex_str) // 2))
```

Then we can simply follow the description steps with this **procedure**:

```python
highest_freq = (0, 0)  # Tuple of type (key_len, dupes_count)
for key_len in range(6, 15):  # Step 1: Set the key length to test (6-14)
    # Step 2: Shift the string by key_len
    shifted_bytes = text_bytes[key_len:] + text_bytes[:key_len]
    # Step 3: Count the characters that are the same in the same position
    frequency = len([x for x, y in zip(text_bytes, shifted_bytes) if x == y])

    # Step 4: Take the highest frequency over different key lengths
    if frequency > highest_freq[1]:
        highest_freq = (key_len, frequency)

key_len = highest_freq[0]
```

Now that we found the most suitable key length, we can proceed with the **cryptoanalysis**.

Like for the **Vigenere** cypher, the key encrypts every `i-th` character of the text.
So, we can group every `(i-th % key_len)` character to try and reconstruct the **key**.
We can achieve it like so:

```python
key_parts = [text_bytes[idx::key_len] for idx in range(key_len)]
```

As an example:

```text
key_len, text = 2, "abcdef"
key_parts = [[a, c, e], [b, d, f]]
```

Now we can assume that the **most common** character is the **space**, so we can **xor** it with the most common
character for every given key index. As for the first part, we can do:

```python
def most_freq_char(string: bytes) -> int:
    # Counter treats bytes like integers
    return Counter(string).most_common()[0][0]

most_freq_chars = [most_freq_char(key_parts[idx]) for idx in range(key_len)]
```

Then we can reconstruct the key by doing `char ^ ord(" ")` for every most-common char. So the key is:

```text
[67, 128, 219, 98, 11, 226, 1, 117]
```

Finally, we can decode the text to get the flag.

```python
decoded_text = ""
for idx, char in enumerate(text_bytes):
    decoded_text += chr(char ^ key[idx % key_len])
```

```text
8eb31c92334eac8f6dacfbaaa5e40294a31e66e0
```
