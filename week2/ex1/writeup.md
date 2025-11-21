## Corrupted hard drive

First up, we can import the "**mysterious numbers**" as a list of tuples in python:

```python
numbers = [(1, 9, 4), (4, 2, 8), (4, 8, 3), (7, 1, 5), (8, 10, 1)]
```

Then, by looking at `book.txt`, we can see that it is conveniently split into **paragraphs** and **lines** of similar 
length. Could the tuples actually be "**coordinates**" for words to find in the file? Sure enough, the first tuple
`(1, 9, 4)` is the word "the".

To implement this in python, we can divide the book in:

- Paragraphs: `contents.split("\n\n")`
- Lines: `paragraph.split("\n")`
- Words: `line.split(" ")`

Finally, for every array, we can access a specific item by the index of the "mysterious numbers", normalized from
`[1..n]` to `[0..n-1]`. Then, assembling the **5 words** indicated by the "mysterious numbers", gives us:

```text
the flag, is Ceremonial plates.
```

So ultimately, the flag is:

```text
Ceremonial plates
```
