function loaded()
 {
    starttime = localStorage["starttime"];

    //check if starttime is there in local storage. 
if (starttime) {
    console.log("fkhshbfksbfs");
    // hide the start button and display the end button. 
    document.getElementById('start_time').value = localStorage["starttime"];
    document.getElementById("start_time_value").style.display = "none"
    document.getElementById("end_time_value").style.display = "block"
    document.getElementById("end_time_value").style.width = "100%"
    document.getElementById("task").value = localStorage["selectedid"];
    document.getElementById("taskshow").innerHTML = localStorage["selectedtext"];
    document.getElementById("task").style.display = "none"
    document.getElementById("description").value = localStorage["description"];
    console.log(localStorage["selectedid"]);
    console.log(localStorage["selectedtext"]);


    // start counter again

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
 }