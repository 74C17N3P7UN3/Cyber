## Cookie monster

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t cookie_monster .
```

Then, we can start the **image** from the GUI and expose the port `8080:5000`.

### Inspecting the page

By visiting the page, we are greeted by a cookie monster. As the name suggests, the challenge involves **cookies**.
After a quick look at the browser's cookie **storage**, we see a `permission` cookie:

```
04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb
```

This could be a **hashed** value, so by checking a website like [crackstation.net](https://crackstation.net/), we see 
that it is the `SHA256` hash of the value `user`.

### Exploiting the logic

Then, by using a website like [online-tools](https://emn178.github.io/online-tools/sha256.html), we can calculate 
the hash of `admin`, which is:

```
8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```

Putting this hash in the browser's storage and sending another request with any `username` and `password`, redirects 
us to a page displaying the **flag**:

```
spritz{thank_you_for_the_cookie}
```
