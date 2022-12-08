function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
  
    // Pad with leading zeros
    hours = hours.toString().padStart(2, '0');
    minutes = minutes.toString().padStart(2, '0');
    seconds = seconds.toString().padStart(2, '0');
  
    var timeString = hours + " : " + minutes + " : " + seconds;
    document.querySelector('.clock-time').textContent = timeString;
  }
  
  setInterval(updateClock, 1000); // update every second
  