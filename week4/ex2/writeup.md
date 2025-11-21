## Ready XOR not

We are given the following three variables:

```python
original_data = "El Psy Congroo".encode("ascii")
encrypted_data = base64_decode("IFhiPhZNYi0KWiUcCls=")
encrypted_flag = base64_decode("I3gDKVh1Lh4EVyMDBFo=")
```

From the challenge's title, we can deduce that we need to **XOR** something.
Since `encrypted_data` is just **random bytes**, it means that it must have been encrypted with a **key**.
To retrieve the key, we can do `original_data ^ encrypted_data`. The key is:

```text
e4Bne4Bne4Bne4
```

We can finally **xor** the `key` with the `encrypted_flag`, to get the **flag**:

```text
Alpacaman
```
