# iotea

## Code
The functional code exists in 3 folders: `device` contains code that would run on the device, `server` contains code that would run on the server, and `databasefiles` contains php scripts that control web app interation with the database.

Data is transmitted via MQTT from the device to the server in JSON format, where it is decoded and sent to the web app / database. The web app and database communicate with each other in respose to user interaction with the web app.

## Website
The website files are in the folder `Website`. The website can be viewed by opening `Website/index.html`. 
