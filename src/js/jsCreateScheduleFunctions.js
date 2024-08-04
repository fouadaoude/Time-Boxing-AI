var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

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
    let taskAmount = document.getElementById('amount');
    let taskAmountDropDown = document.getElementById('taskAmount');
    let taskEntryNav = document.getElementById('taskEntryNav');

    taskAmount.innerHTML = "Task Amount: " + amount;
    
    taskAmountDropDown.classList.toggle("show");    
        
    if (!taskEntryNav.classList.contains("showGrid")) {
        taskEntryNav.classList.toggle("showGrid");    
    }    
    
    amount = Number(amount);

    createTaskNavBar(amount);

}

function createTaskNavBar(amount) {
    let tab = document.getElementById("tab");    
    var taskEntryNav = document.getElementById('taskEntryNav');
    var tabLength = 0;

    while (amount < tabLength || amount > tabLength) {           
        tabLength = countId();
        
        if (amount < tabLength) {                        
            var elem = document.getElementById('tab'+String(tabLength));
            elem.parentNode.removeChild(elem);
            
        }

        else if (amount > tabLength) {     
            var newTab = document.createElement("a");
            newTab.id = "tab"+String(tabLength+1);
            newTab.textContent = "Tab "+String(tabLength+1);
            newTab.href = "#";
                   
            taskEntryNav.appendChild(newTab);
        }

    }        

}


function countId() {
    var count = $('[id^=tab]').length;

    return Number(count);
}

function toggleDropDown(amount) {
    document.getElementById("taskAmount").classList.toggle("show");
}
