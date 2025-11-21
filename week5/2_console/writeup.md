## Console

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t console .
```

Then, we can start the **image** from the GUI and expose the port `8080:80`.

### Inspecting the page

By inspecting the page, we see a client-side **ajax** function that checks the return value from the server:

```javascript
var foo = document.getElementById("p");

function what() {
    var input = document.getElementById("pass").value;
    if (md5(input) == "7b1ece53a46f4a5a2995b9cf901bf457") {
        getThat('Y');
    } else {
        getThat('N')
    }
}

function getThat(string) {
    if (string == 'Y') {
        $.ajax({
            type: 'GET',
            url: '1/key.php',
            success: function(file_html) {
                foo.innerHTML = (file_html)
            }
        });
    } else {
        foo.innerHTML = "Nope";
    }
}
```

From this **script**, we can see that the **flag** is awarded when the function `getThat` is called,
with a string of value `"Y"` as a parameter.

### Exploiting the logic

We can simply call this function ourselves from the **browser's console** like so:

```
>> getThat("Y")
```

This triggers the function's logic, consequently displaying the **flag** on the page:

```
flag{console_controls_js}
```
