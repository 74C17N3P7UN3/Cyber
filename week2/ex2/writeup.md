## Sherlock's mystery

A first look at `challenge.txt`, reveals a strictly lowercase book, except for some mysterious **uppercase** 
characters. Iterating over the book and saving only those characters, gives us a string of this type:

```text
ZEROONEZEROZEROZEROZEROONEZEROZEROONE...
```

After converting it into actual **binary code**, we can assume that it could be **ASCII text**. So, by dividing the 
binary string into **byte chunks**, and converting them to their ASCII equivalent, we get the flag:

```text
BITSCTF{h1d3_1n_pl41n_5173}
```
