function validate()
{
    if(document.getElementById("username").value == "brbiamafk"
       && document.getElementById("password").value == "Peepeepoopoo69!" )
    {
        alert("Login successful.");
        location.href="myprofile.html";
    }
    else
    {
        alert( "Incorrect login credentials." );
    }
}
