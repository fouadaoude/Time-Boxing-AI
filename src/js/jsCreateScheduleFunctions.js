function buttonStayPressed(type) { 
    let pressed = buttonPressed();

    let button = ""
    
    if (type === 'day') {        
        button = document.getElementById("scheduleButtonDay");        
    }
    
    else if (type === 'week') {
        button = document.getElementById("scheduleButtonWeek");
    }
    
    else if (type === 'month') {
        button = document.getElementById("scheduleButtonMonth");
    }
    //alert(button.classList);

    if (pressed === false || button.classList.contains('active')) {
        button.classList.toggle('active');
    }
    
}

function buttonPressed() {
    dayButton = document.getElementById("scheduleButtonDay"); 
    weekButton = document.getElementById("scheduleButtonWeek"); 
    monthButton = document.getElementById("scheduleButtonMonth");

    if (dayButton.classList.contains('active')) {
        return true;
    }

    else if (weekButton.classList.contains('active')) {
        return true;
    }

    else if (monthButton.classList.contains('active')) {
        return true;
    }
    
    else {
        return false;
    }

}

function taskAmountDisplay(amount) {
    let taskAmount = document.getElementById('taskAmount');

    taskAmount.innerHTML = "Task Amount: " + amount;
}