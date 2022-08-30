
# FastAPI
![alt text](https://github.com/llraekll/llraekll/blob/main/images/fastapi.png?raw=true)
This project is built on FastAPI framework based on a social media platform performing actions such actions User and Post creation using Postgres database, user authentication using hashed passwords and issusing JWT tokens hosting on Heroku, setting up and deploying on a Virtual Machine, creating CI/CD pipeline with github jobs.
* User creation
* User authentication    
* User login timeout with JWT tokens
* Creating Post linked to the user table
* Reading a Post
* Updating a Post
* Deleting a Post
* Voting a Post  



### Deploy on Heroku
![alt text](https://github.com/llraekll/llraekll/blob/main/images/Heroku.png?raw=true)
* Create a Procfile mentioning your app’s web server
* Create a requirements.txt file for Heroku to identify the language
* Ensure there are no unused libraries mentioned in the source code
* Add and commit source code, create a Heroku remote as mentioned on Heroku
* Deploy your code 

```bash
    git push heroku main
```

![alt text](https://github.com/llraekll/llraekll/blob/main/images/DigitalOcean.png?raw=true)

### Deploy on Ubuntu VM
* Create a droplet on digital ocean
* login into your VM using command promt/ windows terminal
```bash
    ssh root@IP address
```
* Configure user with admin rights 
* Python3 comes pre-installed 
* Install PIP and Postgres
* Configure config files on the VM
* Setup the database using postgres
* Make a directory to clone your github repo
* Link your domain to the IP address of your droplet
![alt text](https://github.com/llraekll/llraekll/blob/main/images/ubuntu.png?raw=true)
