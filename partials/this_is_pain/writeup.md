## This is pain

By inspecting the **cyphertext**, we see that it is encoded with bytes of literals **Ones** and **Zeros**.
So the first step is to replace them with actual **bits**:

```python
with open("ciphertext.txt") as file:
    contents = file.read()

binary_string = (contents
                 .replace("Z", "0")
                 .replace("O", "1"))
```

Then, we can convert the **bytes** into characters like so:

```python
base64_string = ""
for byte in binary_string.split():
    base64_string += chr(int(byte, 2))
```

Which gives us a string encoded in **Base64** as output. After decoding it with the following code, we get a text:

```python
from base64 import b64decode

decoded_bytes = b64decode(base64_string.encode("ascii"))
print(decoded_bytes.decode().strip())
```

```
NKRG: ZAF KBSYV WY EQZ R'W VARGI KJJ TQRB?
HFT YPYG RX R TAJV ZAF EQZ, R VAFHT PYOZ BTOAGIJZ TQKT TQY SGAEJYVIY EAFJV CQKGIY KGZTQRGI KT KJJ HFT 
JYT'B DFBT BKZ TQKT R TKSY TQY TRWY TA YLNJKRG RT TA ZAF. EQKT VA ZAF TQRGS EAFJV QKNNYG TQYG? WZ IAKJ 
RB TA XFJXRJJ TQY VOYKW YPYG DROKZK BYGBYR EKB FGKHJY TA KCQRYPY TQKT RB TA COYKTY NYKCY KGV HORGI KHAFT 
DFBTRCY. AQ R BYY TQKT RB GAHJY AX ZAF TQKT EAFJV HY DFBTRCY. QAEYPYO EQKT KHAFT WZ XKWRJZ?

[...]
```

This is quite clearly a **substitution cypher**, so by using a website like
[guballa.de](https://www.guballa.de/substitution-solver), we can easily crack the **dictionary**:

```
Original:   abcdefghijklmnopqrstuvwxyz
Mapped:     oscjwunbglaxqprvhiktzdmfey
```

```
PAIN: YOU ASKED ME WHY I'M DOING ALL THIS?
BUT EVEN IF I TOLD YOU WHY, I DOUBT VERY STRONGLY THAT THE KNOWLEDGE WOULD CHANGE ANYTHING AT ALL BUT 
LET'S JUST SAY THAT I TAKE THE TIME TO EXPLAIN IT TO YOU. WHAT DO YOU THINK WOULD HAPPEN THEN? MY GOAL 
IS TO FULFILL THE DREAM EVEN JIRAYA SENSEI WAS UNABLE TO ACHIEVE THAT IS TO CREATE PEACE AND BRING ABOUT 
JUSTICE. OH I SEE THAT IS NOBLE OF YOU THAT WOULD BE JUSTICE. HOWEVER WHAT ABOUT MY FAMILY? 

[...]
```

At the end of the text, we find the **flag**:

```
SPRITZ{SHINRA_TENSEI_EVERYWHERE}
```
