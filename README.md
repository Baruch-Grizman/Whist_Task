# Whist DevOps Task

This application is part of **Whist Task** for DevOps.
The purpose of the task is to run a web app on 3 instances using Nginx load balancer.
Version control is managed in `GIT`

## Task Description
### An explanation of the various files in the project

```
Whist_Task/
│
├── app/
│   ├── Dockerfile
│   ├── flasklocalip.py
│   └── requirements.txt
│
├── docker-compose.yml
├── nginx.conf
└── README.md
```
### app folder
flasklocalip.py
The purpose of the app is to display the local host IP in the browser using `FLASK` and `HTML` for page creation and publishing,
the Web Server Gateway Interface (WSGI) is used with `Gunicorn`. 
The app code is written using `Python`.

requirements.txt
This file defines outside Python dependencies and their versions for our app.
our requirements is: `FLASK` and `Gunicorn`

Dockerfile
This file defines the instructions to create Docker Image.
the file also contains the requirements in order for the app to run correctly, and the command to run it once deployed.

### root folder
nginx.conf
this is the configuration file for Nginx server.
inside it, we configured two blocks:
events - to set the amount of `worker_connections`which is basically the number of clients that can connect to the Nginx server.
http - this block listen to port `80` on the server, and use it as a reverse proxy. It accepts incoming connections and decides where they should go next.

docker-compose.yml
This file defines the instructions to deploy Docker images.
first we deploy our app, and expose it in port `9090`
second, once the app is deployed we deploy Nginx image, and copy `nginx.conf`file we created to our Nginx server.

README.md
This is a `Markdown` file documenting the purpose and usage of our project

## Execution

 1. Clone this repository
 2. From terminal use the command `docker-compose up -d --build --scale app=3`, and wait for the Deployment to finish the build process.
 !https://ibb.co/bmPjTrp
 3. Open browser at `http://localhost:9090/`
 4. For each page refresh you will cycle between 3 different IP's, which represent 3 different instances.
 5. Once done, use the command `docker-compose down`, to close all instances and Nginx server.