function validate()
{
  var username=document.getElementByID("username").value;
  var password=document.getElementByID("password").value;
  if (username=="brbiamafk"&& password=="Peepeepoopoo69!")
{
      alert("Login successful");
      return false;
}
else
{
      alert("Incorrect username or password. Login failed");

}
}
