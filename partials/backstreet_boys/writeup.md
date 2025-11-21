## Backstreet Boys

By looking at `encrypt.py`, we can see that the key is being **extended repeatedly** up to the flag's length.
Then, we see that the encryption works by shifting the alphabetic characters, and keeping the rest the same:

```python
offset = 97

if char_plain.isalpha():
    encrypted_char = chr((ord(char_plain) + ord(char_key) - 2 * offset) % 26 + offset)
else:
    encrypted_text += char_plain
```

What the shifting is doing, is basically taking the **index** of `char_plain` and adding the **index** of `char_key`,
since the **ASCII** value of `a` is **97**, and then converting it back into a **character**.

Now, we can simplify a bit the logic to achieve the same result: **subtracting** the `char_key` to the final 
`encrypted_char`. First of all, we declare the final `encrypted_text` and the used `key`:

```python
ciphertext = "ltctfd{p-peye-mp-raee-ieu}"
key = "tellmewhy"
```

Then, while going through the **ciphertext**, if we encounter an alphabetic character, we shift it.
Otherwise, we simply copy it.

```python
from string import ascii_lowercase

solution = ""
for idx, char in enumerate(ciphertext):
    if char in ascii_lowercase:
        char_idx = ascii_lowercase.index(char)
        key_idx = ascii_lowercase.index(key[idx % len(key)])
        solution += ascii_lowercase[(char_idx - key_idx) % 26]
    else: solution += char
```

With this, we get the original **flag**:

```
spritz{i-want-it-that-way}
```
