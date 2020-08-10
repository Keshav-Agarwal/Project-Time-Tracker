function upcounter(start) {

  // get time when started
  var starttime = new Date().getTime();

var x;

if (start) {

  //hide start button, display end button
  document.getElementById("start_time_value").style.display = "none"
  document.getElementById("end_time_value").style.display = "block"
  document.getElementById("end_time_value").style.width = "100%"
  var e = document.getElementById("task");
  var value = e.options[e.selectedIndex].value;
  var text = e.options[e.selectedIndex].text;
  localStorage.setItem("selectedid", value);
  localStorage.setItem("selectedtext", text);
  localStorage.setItem("description", document.getElementById("description").value);
  localStorage.setItem("starttime", starttime);
  document.getElementById("task").value = localStorage["selectedid"];
  document.getElementById("taskshow").innerHTML = localStorage["selectedtext"];
  document.getElementById("task").style.display = "none"
  document.getElementById("description").value = localStorage["description"];



x = setInterval(function() {

    var now = new Date().getTime();
      
    var distance = -(starttime - now);
      

    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("timer").innerHTML = hours + "h "
    + minutes + "m " + seconds + "s ";
    document.getElementById("timer").name = x;
  }, 1000);
}

else {
  document.getElementById("start_time_value").style.display = "block"
  document.getElementById("start_time_value").style.width = "100%"
  document.getElementById("end_time_value").style.display = "none"
  x = document.getElementById("timer").name;
  localStorage.removeItem("starttime");
  localStorage.removeItem("selectedid");
  localStorage.removeItem("selectedtext");
  localStorage.removeItem("description");
  clearInterval(x);
}

}