## Password generator

To generate a random password of length 10, we can use `string.ascii_letters` and `string.digits` to get a list of 
all alphanumeric characters, and `random.choice` to automatically choose a random character from the previous two 
lists. Wrapping this process in a for loop of `range(10)` gives us a random password of the desired length.
