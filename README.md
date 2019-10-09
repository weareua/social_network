# Social Network
It's a web based application that:  
- generates n number of users and fills posts and likes for them  
- provides the REST API with the possibility of authorization (login/register), new post creation, posts liking functionality  


![Alt text](screenshot.png =250px)


## Stack
This application is built using Django and Django REST framework and JWT.

## Requirements
Social Network uses python language version 3 and above. You can install it using this [article](https://realpython.com/installing-python/). 
Also you should have installed [pip](https://github.com/pypa/pip) and [virtualenv](https://github.com/pypa/virtualenv) in order to deploy application locally.

## Installation
Please follow these steps if you want to run the local copy of the app:

I. Download archive with project and unzip it
II. Move into unzipped folder using console like this:
```
$ cd social_network
```
III. Create virtual environment to isolate application specific dependencies. Please keep in mind that this instruction will not work for windows user. If you are using windows try to find another way to install virtual environment with python 3 and above.
```
$ virtualenv venv -p /usr/bin/python3
```
IV.  Enable virtual environment
```
$ source venv/bin/activate
```
V. Install application dependencies in the isolated environment
```
$ pip install -r requirements.txt
```
VI. Create necessarry tables in the database:
```
$ python manage.py migrate
```
VII. Populate database with automatically generated users, posts and likes:
```
$ python manage.py populate
```
VIII. Register on [Hunter](https://hunter.io/) and obtain its API key
We'll use this service to verify potential user email address.  
When you'll register your self there, you have to get API key and place it as the value for variable HUNTER_API in the env file. You can find it using this path:  
```  
core/.env  
```
IX. Run application's local server:
```
$ python manage.py runserver
```
## Usage
If you are done with installation process, you can visit [http://localhost:8000/](http://localhost:8000/) url and see Social Network working.
On the front page you should see table with posts data. 

API for Social Network is divided by access level.
### Public endpoints:

[/api/auth/register/](http://localhost:8000/api/auth/register/)  
[/api/auth/token/](http://localhost:8000/api/auth/token/) (Login purpose)  
[/api/posts/](http://localhost:8000/api/posts/)(GET)  

### Authorized endpoints:  
To authorize yourself you have to use access token from [/api/auth/token/](http://localhost:8000/api/auth/token/) endpoint  
[/api/users/](http://localhost:8000/api/users/)  
[/api/posts/](http://localhost:8000/api/posts/)(POST)  
[/api/impact/post/](http://localhost:8000/api/posts/)(POST, endpoint to like/unlike posts)  
