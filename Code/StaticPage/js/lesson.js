function sendComment(str)
{
console.log("str: " + str);
var xmlhttp;    
if (str=="")
  {
  alert("Empty content.");
  return;
  }
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("POST", "/comment/create/", true);
xmlhttp.send(str);
console.log("str: " + str);
}

function shareFile(file) {
  var xmlhttp;
  if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  }
  else {// code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.open("POST", "/meterial/create/", true);
  xmlhttp.send(file);
}
/*
window.onload = function() {
  // alert("hello");
  var body = document.body;
  var msg = document.createElement("div");
  msg.innerHTML = "This is a message";
  msg.className += "bg-info text-center ";
  var remove = document.createElement("span");
  remove.attributes["data-role"] = "remove";
  var icon = document.createElement("i");
  icon.className += " "
  remove.appendChild(document)
  msg.appendChild(remove);
  body.appendChild(msg);
}
*/