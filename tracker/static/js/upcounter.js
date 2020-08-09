function upcounter(start) {
var starttime = new Date().getTime();

var x;

if (start) {
  document.getElementById("start_time_value").style.display = "none"
  document.getElementById("end_time_value").style.display = "block"
  document.getElementById("end_time_value").style.width = "100%"

x = setInterval(function() {

    // Get today's date and time
    var now = new Date().getTime();
      
    // Find the distance between now and the count down date
    var distance = -(starttime - now);
      
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
      
    // Output the result in an element with id="demo"
    document.getElementById("timer").innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";
    document.getElementById("timer").name = x;
    
    console.log(days, hours, minutes, seconds);

  }, 1000);
}

else {
  document.getElementById("start_time_value").style.display = "block"
  document.getElementById("start_time_value").style.width = "100%"
  document.getElementById("end_time_value").style.display = "none"
  x = document.getElementById("timer").name
  clearInterval(x);
}

}