function removeHomeButtons() {
    let homeButtons = document.getElementById('homeButtons');

    homeButtons.classList.add('animateFadeOut');

    setTimeout(function () {
        homeButtons.parentNode.removeChild(homeButtons)
      }, 400); // 400 is the same time as the css animation

}

function removeOptionH1() {
    let h1 = document.getElementById('optionH1');

    h1.classList.add('animateFadeOut');

    setTimeout(function () {
        h1.parentNode.removeChild(h1)
    }, 400); // 400 is the same time as the css animation
}

function removeHomeLogo() {
    let logo = document.getElementById('homeLogo');

    logo.classList.add('animateFadeOut');

    setTimeout(function () {
        logo.parentNode.removeChild(logo)
      }, 400); // 400 is the same time as the css animation
}

function connectHomeContainer() {
    let homeContainer = document.getElementById('homeContainer');
    let optionColumn = document.getElementById('option');
    let logoColumn = document.getElementById('homeLogoContainer');

    homeContainer.classList.add('animateHomeContainerGap');       

    setTimeout(function () {
        //optionColumn.parentNode.removeChild(optionColumn);
        homeContainer.style.gap = "0%";        
        optionColumn.style.borderLeft = "none";
        logoColumn.style.borderRight = "none";
      }, 400); // 400 is the same time as the css animation

      setTimeout(function () {
        optionColumn.classList.add('animateFadeBorders');
        logoColumn.classList.add('animateFadeBorders');
      }, 500);
      

      setTimeout(function () {
        logoColumn.style.border = "none";     
        optionColumn.style.border = "none";   
        homeContainer.remove();
      }, 600); // 400 is the same time as the css animation

}

function homeButtonPressAnimation(type) {
    // Remove buttons first thing
    removeHomeButtons();

    // Remove "select an option" <h1> second
    removeOptionH1();
    
    // Remove home logo third
    removeHomeLogo();

    // Connect the gap in homeContainer fourth
    connectHomeContainer();

    // redirect to .html last
    if (type === "view") {
        setTimeout(function () {
            location.replace("viewSchedule.html");
        }, 500);
    }

    else if (type === "create") {
        setTimeout(function () {
            location.replace("createSchedule.html");
        }, 500);
    }
    

}