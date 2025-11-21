## Shifting chars

In order to shift the characters in the alphabet, we need to:

- Get their index: `ascii_lowercase.index(character)`
- Apply the shift: `(char_idx + shift_amount) % 26`
- Convert back the index to the character: `ascii_lowercase[shifted_idx]`

Thanks to `string.ascii_lowercase`, we don't have to worry about all ASCII values.
