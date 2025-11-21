## Biscuit parade

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t biscuit_parade .
```

Then, we can start the **image** from the GUI and expose the port `8080:5000`.

### Inspecting the page

By visiting the page, we are greeted by a frightening Micheal Jackson.
The name of the challenge suggests that some **cookies** are involved.
After a quick look at the browser's cookie **storage**, we see a `permission` cookie:

```
user
```

### Exploiting the logic

Since this is a **client-side** cookie, we can simply replace it with `admin` and send a request with any `username` 
and `password`. Doing this redirects us to a page displaying the **flag**:

```
spritz{N3zuk0-chaaaaan}
```
