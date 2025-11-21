## Fady's mistake

Looking at `zero_one.txt`, we can see a list of "**ZERO**"s and "**ONE**"s.
By converting them into their binary form and then to their **ASCII** equivalent, as done in the previous exercise,
we get the following string:

```text
Li0gLi0uLiAu...Li4tLSAtIC0tLSAtIC0uLi0gLQ==
```

From the trailing `==`, we can assume that it could be a **base64** string. Decoding it gives us:

```text
.- .-.. . -..- -.-. - [...] - --- - -..- -
```

**Morse code?!** Oh, well... Unfortunately, python doesn't have a nice way to convert it into ASCII, but by using a
known **convertion table** in a small utility function, we can decode it.

```python
def morse_to_ascii(morse_str: str) -> str:
    morse_code_dict = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        ...: ...
    }

    ascii_string = ""
    for character in morse_str.split(" "):
        ascii_string += morse_code_dict[character]
    return ascii_string
```

Finally, after **4 layers** on encoding, we got the flag:

```text
ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT (ALEXCTF{TH15_1S_5UP3R_5ECR3T_TXT})
```
