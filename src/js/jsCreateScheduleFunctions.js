 var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

class Task {
    constructor(tab) {
        this.tab = tab;
        //this.taskName = taskName;
        //this.taskDesc = taskDesc;
        //this.taskImportance = taskImportance;
        //this.taskTime = taskTime;
    }

    create() {
        let taskEntryNav = document.getElementById('taskEntryNav');
        let taskEntryContainerLeft = document.getElementById('taskEntryContainerLeft');
        let taskEntryContainerRight = document.getElementById('taskEntryContainerRight');
        let currentTaskId = document.getElementsByClassName('clicked')[0].id

        let currentTask = document.getElementById(currentTaskId);


        // Check is current tab clicked does not already have values. If values exist. Keep them.
        //document.querySelector('.myClassName').id

        //taskNameLabel.setAttribute("for", currentTask)
        if (this.tab) {
            console.log("YES",currentTask); 
            var taskFormDiv = document.createElement("form");
            var taskNameLabel = document.createElement("label");
            var taskNameEntry = document.createElement("");
            taskNameLabel.textContent = "Task Name";
            
            taskEntryContainerLeft.appendChild(taskFormDiv);
        }
        

    }
}

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

function buttonPressed(tab) {
    var tabClicked = document.getElementById(tab);
    
    if (!tabClicked.classList.contains('clicked')) {
        tabClicked.classList.toggle('clicked');
    }

    for (var id=1;id <= 5;id++) {
        var tabID = "tab"+String(id);
        var currentTab = document.getElementById(tabID);            
        if (currentTab.classList.contains('clicked') && tabClicked !== currentTab) {
            currentTab.classList.toggle('clicked');
        }
    }
}

function taskDisplay(amount) {
    let taskAmount = document.getElementById('amount');
    let taskAmountDropDown = document.getElementById('taskAmount');
    let taskEntryNav = document.getElementById('taskEntryNav');
    let taskEntryContainerLeft = document.getElementById('taskEntryContainerLeft');
    let taskEntryContainerRight = document.getElementById('taskEntryContainerRight');

    taskAmount.innerHTML = "Task Amount: " + amount;
    
    taskAmountDropDown.classList.toggle("show");    
        
    if (!taskEntryNav.classList.contains("showNavGrid")) {
        taskEntryNav.classList.toggle("showNavGrid");   
        taskEntryNav.classList.add("nav"); 
        taskEntryContainerLeft.classList.add("showTaskLeftGrid");
        taskEntryContainerRight.classList.add("showTaskRightGrid");
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
            newTab.style.textDecoration = 'none !important';
            newTab.setAttribute("onClick", "buttonPressed('"+String(newTab.id)+"'); new Task('"+String(newTab.id)+"').create()");

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
