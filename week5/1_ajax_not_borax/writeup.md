## Ajax not borax

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t ajax_not_borax .
```

Then, we can start the **image** from the GUI and expose the port `8080:80`.

### Inspecting the page

By inspecting the page, we see a client-side **ajax** function that checks the return value from the server:

```javascript
// For element with id='name', when a key is pressed run this function
$('#name').on('keypress', function() {
    // get the value that is in element with id='name'
    var that = $('#name');
    $.ajax('webhooks/get_username.php?username=' + that.val(), {}).done(function(data) {
        data = data.replace(/(\r\n|\n|\r)/gm, ""); // remove newlines from returned data
        if (data == MD5(that.val())) { // see if the data matches what the user typed in
            that.css('border', '1px solid green'); // if it matches turn the border green
            $('#output').html('Username is correct'); // state that the user was correct
        } else { // if the user typed in something incorrect
            that.css('border', ''); // set input box border to default color
            $('#output').html('Username is incorrect'); // say the user was incorrect
        }
    });
});
// dito ^ but for the password input now
$('#pass').on('keypress', function() {
    var that = $('#pass');
    $.ajax('webhooks/get_pass.php?username=' + $('#name').val(), {}).done(function(data) {
        data = data.replace(/(\r\n|\n|\r)/gm, ""); // remove newlines from data
        if (MD5(data) == MD5(that.val())) {
            that.css('border', '1px solid green');
            $('#output').html(data);
        } else {
            that.css('border', '');
            $('#output').html('Password is incorrect');
        }
    });
});
```

We are really interested in these two server requests:

```
webhooks/get_username.php?username=`input`
webhooks/get_pass.php?username=`username`
```

### Exploiting the logic

By sending a request to the first **URL**, whatever the input, we get the **MD5** hash of the username, as suggested 
by this if condition `response == MD5(input.val())`, which is:

```
c5644ca91d1307779ed493c4dedfdcb7
```

By using [crackstation.net](https://crackstation.net/) we can **crack** the hash, and find the corresponding username:

```
tideade
```

Now we can send a request to the second URL, with the found username as a **parameter** to get its password:

```
ZmxhZ3tzZDkwSjBkbkxLSjFsczlISmVkfQ==
```

The two leading equal signs, suggest that the flag is encoded in **base64**, so after decoding it we get:

```
flag{sd90J0dnLKJ1ls9HJed}
```
