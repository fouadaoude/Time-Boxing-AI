//main.js
const { app, BrowserWindow } = require('electron');

let mainWindow;

function createWindow() {
    var width = window.innerWidth;
    var height = window.innerHeight;

    console.log(width)

    mainWindow = new BrowserWindow({
        width: 600,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    mainWindow.loadFile('index.html');

    mainWindow.on('closed', function() {
        mainWindow = null;
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', function() {
    if(process.platform !== 'darwin') app.quit();
});

app.on('activate', function() {
    if(mainWindow === null) createWindow();
});