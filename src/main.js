//main.js
const {app, BrowserWindow} = require('electron');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 650,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    mainWindow.loadFile('index.html');

    mainWindow.on('closed', function() {
        mainWindow = null;
        app.quit()
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', function() {
    if(process.platform !== 'darwin') {
        console.log('HELOOOOOO')        
        app.quit()
        
    } 
});

/*app.on('activate', function() {
    if(mainWindow === null) {
        createWindow()
    } 
});*/

// Load up to date GitHub files
