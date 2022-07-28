
function myFunction() {
  let txt;
  let r = confirm("Press a button!");
  if (r == true) {
    txt = "You pressed OK!";
  } else {
    txt = "You pressed Cancel!";
  }
  document.getElementById("demo").innerHTML = txt;
}

// This file not working ....... so try later ....... 
// But use other delete confirmation >>> <input onclick="return confirm('Are you sure you want to delete this post?');" type="submit" class='btn btn-danger btn-sm my-3 font-weight-normal' value="Delete">