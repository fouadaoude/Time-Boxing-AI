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

    createTest() {
        var taskEntryContainerLeft = document.getElementById('taskEntryContainerLeft');
        var taskCount = 1;

        while (this.tab >= taskCount) {
            var taskForm = document.createElement("form");
            var taskNameLabel = document.createElement("label");
            var taskNameInput = document.createElement("input");
            var currentTaskId = "tab" + String(taskCount);


            taskForm.id = currentTaskId + "formLeft";
            taskForm.classList.toggle('clickedForm');

            taskNameInput.type = "text";
            taskNameInput.id = currentTaskId + "inputLeft";

            taskNameLabel.textContent = "Task Name";
            taskNameLabel.setAttribute("for", taskNameInput.id);

            taskForm.appendChild(taskNameLabel);
            taskForm.appendChild(taskNameInput);
            taskEntryContainerLeft.appendChild(taskForm);

            taskCount += 1;
        }

        this.hideForms();
    }

    create() {
        let taskEntryNav = document.getElementById('taskEntryNav');
        let taskEntryContainerLeft = document.getElementById('taskEntryContainerLeft');
        let taskEntryContainerRight = document.getElementById('taskEntryContainerRight');
        let currentTaskId = document.getElementsByClassName('clicked')[0].id

        let currentTask = document.getElementById(currentTaskId);


        // Check is current tab clicked does not already have values. If values exist. Keep them.
        //document.querySelector('.myClassName').id
        var formId = currentTaskId + "formLeft";        
                      

        if (this.tab && !this.formExists(formId)) {    
            
            var taskForm = document.createElement("form");
            var taskNameLabel = document.createElement("label");
            var taskNameInput = document.createElement("input");
            
            taskForm.id = currentTaskId + "formLeft";
            taskForm.classList.toggle('clickedForm');

            taskNameInput.type = "text";
            taskNameInput.id = currentTaskId + "inputLeft";

            taskNameLabel.textContent = "Task Name";
            taskNameLabel.setAttribute("for", taskNameInput.id);
            

            taskForm.appendChild(taskNameLabel);
            taskForm.appendChild(taskNameInput);
            taskEntryContainerLeft.appendChild(taskForm);
        }
        
    }
        
    hideForms() {  
        // hideForms() is currently broken and needs overhaul. Friday 8/9 6:16am
        let formAmount = countFormByClass("clickedForm");
        var thisForm = document.getElementById(thisFormId);

        var formId = "tab" + String(x) +"formLeft";
        formId = String(formId);
        var form = document.getElementById(formId);            

        while (formAmount > 1 || form === thisForm) {            
            formAmount = countFormByClass("clickedForm");
            
            thisFormId = this.tab + "formLeft";
            thisForm = document.getElementById(thisFormId);

            formId = "tab" + String(x) +"formLeft";
            formId = String(formId);
            form = document.getElementById(formId);            
            
            if (form) {
                if (form === thisForm) {
                    form.classList.remove("showForm");
                    form.classList.add("clickedForm");
                }                
                
                else if (formAmount > 1 && form !== thisForm) {
                    form.classList.remove("clickedForm");
                    form.classList.add("showForm");                                           
                }
            }
            x+=1;       
        }
    }

    formExists(formId) {
        var form = document.getElementById(formId);
        
        if (form) {
            return true;
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

    // Check how many tabs the user selected
    var taskAmount = document.getElementById("taskEntryNav").children.length;

    // Loop through all the open tabs and check which one was clicked and toggle colored underline
    for (var id=1;id <= taskAmount;id++) {
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

    // while amount of selected tabs is less than the current tabLength
    // or while the selected tab amount is greater than current tabLength

    while (amount < tabLength || amount > tabLength) {           
        tabLength = countId();
        
        // check if the selected tab amount is less than the current tabLength
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
    
    buttonPressed("tab1");
    new Task(amount).createTest();
}

function countFormByClass(form) {
    var formAmount = document.getElementsByClassName(form).length;

    return formAmount;
}

function countId() {
    var count = $("a[id*='tab']").length;
    //var count = $('[id^=tab]').length;

    return Number(count);
}

function toggleDropDown(amount) {
    document.getElementById("taskAmount").classList.toggle("show");
}
