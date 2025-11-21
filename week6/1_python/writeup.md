## Python

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t python .
```

Then, we can start the **image** from the GUI and expose the port `8080:5000`.

### Inspecting the page

By visiting the page, we are given a url to see the page's **source code**.
After beautifying it, we get the following code:

```python
@app.route("/flag")
def get():
    if request.method == "GET":
        ip = request.args.get("ip")
        port = request.args.get("port")
        flag = open("flag.txt").readline()
        allowed = {
            "allowed_ip" : "8.8.8.8",
            "allowed_port" : port,
            "allowed_flag": flag
        }
        
        if ip and ip != "" and port and port != "":
            if port.isdigit():
                if ip == allowed.get("allowed_ip"):
                    subprocess.Popen(f"cat flag.txt > /dev/tcp/{ip}/{port}", shell=True, executable="bash")
                    return ("SUCCESS: The flag have been sent to DST IP %s and DST PORT %s\n") % (ip, port)
                else: return ("You have chosen IP " + ip + ", but only %(allowed_ip)s will receive the key\n") % (allowed)
            else: return ("Port invalid\n")
        else: return ("Please choose an IP and a PORT\n")
    else: return ("FAIL: Method HTTP not allowed (%s)\n") % (request.method)
```

At a first glance, it would seem like we need to use **IP** `8.8.8.8` and **any port** in order to get sent the flag.
However, the command that gets executed is the following:

```commandline
cat flag.txt > /dev/tcp/{ip}/{port}
```

This simply **echoes** the contents of the file `flag.txt` and puts it into a file named as the **port value**, in the 
directory `/dev/tcp/8.8.8.8`.

So we are truly interested in this line here:

```python
return ("You have chosen IP " + ip + ", but only %(allowed_ip)s will receive the key\n") % (allowed)
```

### Exploiting the logic

It raises suspicion that our given **IP** gets **concatenated** and not accessed directly. This allows us to exploit 
the **modulo operator**. Since the flag is saved in the same **dictionary** as the `allowed_ip`, under the 
`allowed_flag` key, we can actually pass `%(allowed_flag)s` as the IP and any given port works.

By interacting with the website, or by directly visiting the following **URL** yields the **flag**.

```
http://localhost:8080/flag?ip=%25%28allowed_flag%29s&port=8080
```

```
INSA{Y0u_C@n_H@v3_fUN_W1Th_pYth0n}
```
