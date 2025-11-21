## Caesar is everything

As cited in the clue: "caesar" is everything. We can try a **Vigenere** cyper, as the **ciphertext** contains quite 
a few repetitions and the word "caesar" could be the **key**.

As a clever trick, instead of repeating the key to match the ciphertext's length, we can iterate over the ciphertext,
and access the key's index `%` its length like this:

```python
for idx, char in enumerate(ciphertext):
    key_char = key[idx % len(key)]
```

Then, we can subtract the key's char from the ciphertext's to obtain the initial value.
We can use `string.ascii_lowercase` to simplify the convertion from character to int, and vice versa.

In the end, we get the flag:

```text
theforceisstrongwiththisone
```
