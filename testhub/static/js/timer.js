// Create a function that take display and duration as argument
function startTimer(duration, display) {
    let timer = duration, minutes, seconds;

    
    let countDown = setInterval(() => {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        
        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            window.location.href = "/";
            clearInterval(countDown);
        }
    }, 1000);
}

// Activate the startTimer function when the page load
window.onload = () => {
    let duration = 60 * 5;

    let display = document.getElementById('countdown');

    startTimer(duration, display);
};