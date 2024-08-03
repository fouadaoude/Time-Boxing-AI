//main.js
const {app, BrowserWindow} = require('electron');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1000,
        height: 750,
        webPreferences: {
            nodeIntegration: true,
        },
    });

    mainWindow.loadFile('src/index.html');

    mainWindow.on('closed', function() {
        mainWindow = null;
        app.quit();
    });
}

app.whenReady().then(createWindow);
