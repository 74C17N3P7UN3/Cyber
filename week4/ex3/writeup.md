## Top secret

By analyzing the **encryption** file, we can notice two things:

- In first part of the file, a `key` is generated of the same length as the `message`, and then **XORed**
- The rest of the encrypted file, is the `cur_time` **XORed** with these bytes `[0x88]`

Since in python, `time.time()` returns a `float`, once it is converted to a string, it has **length 18**.
We can then split the `top_secret` file contents into two parts:

```python
with open("top_secret.txt", "rb") as file:
    contents = file.read()

msg_bytes, time_bytes = contents[:-18], contents[-18:]
```

We can get back the time at which the message was **encrypted** like so:

```python
cur_time = xor_bytes(bytes([0x88] * 18), time_bytes)
```

Since the `random.seed` was set on the encryption, we can arbitrarily reconstruct the `key`:

```python
set_random_seed(cur_time)
key = bytes([randrange(256) for _ in msg_bytes])
```

Finally, we have all we need to **XOR** back the original message, giving us the **flag**:

```text
34C3_otp_top_pto_pot_tpo_opt_wh0_car3s
```
