## Brute force dictionary

Given the absence of any type of **key**, and after trying **incremental shifts** or simple shifts in a range, we 
can try by brute forcing the **ciphertext** with a **substitution dictionary**.

The idea behind it is that we start with a dictionary like this:

```python
subs_dict = { "A": "A", "B": "B", "C": "C", ...: ... }
```

And slowly change the characters' **mapping** to end up to something like this:

```python
subs_dict = { "A": "F", "B": "E", "C": "B", ...: ... }
```

We could start by assuming that the last long word is the **flag**, and that the previous word actually spells "FLAG".
Also, the "K'Q" in the ciphertext could be "I'M", and so we can associate these characters for now:

```python
subs_dict = { "W": "F", "A": "L", "F": "A", "I": "G", "K": "I", "Q": "M", ...: ... }
```

Doing this **bit by bit**, slowly moves us to the decrypted text while we populate the dictionary.
In the end, we solve the cryptogram, and the flag is:

```text
DOINGTHISBYHANDISMOREFUNTHANANONLINETOOL
```
