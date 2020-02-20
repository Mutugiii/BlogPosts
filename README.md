[![codebeat badge](https://codebeat.co/badges/145d2c50-8ebd-4bd7-8c4e-7ebfb91cfac0)](https://codebeat.co/projects/github-com-mutugiii-blogposts-master)

# Microblog

## Description
This is a python flask crud web app that allows a user to sign up and post, view and provide feedback on various Microblog that are posted by other users

## Author


[**Mutugi**](https://github.com/mutugiii)

## Features
- Log in and Sign up - User and Writer
- Welcome Mail
- Subscription Mail
- Create Blog
- Update Profile
- Writer Delete and Update blog post

## User Stories 
As a user of the web application you will be able to:

1. View Microblog based on categories
2. Sign up and log in
3. Receive welcome mail
4. Subscribe to a mailing list
5. Comment on a Microblog and view other comments
6. Edit user profile: View all your posted Microblog; Update bio and profile image

As a Writer I will be able to
1. View Microblog based on categories
2. Sign up and log in
3. Receive welcome mail
4. Add a Microblog 
5. Comment on a Microblog and view other comments
6. Edit user profile: View all your posted Microblog; Update bio and profile image
7. Delete a blog post
8. Update a blog post

## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

Clone the repository and cd to `Microblog`

## Running the App
* Create a virtual environment
    ```$ python3.6 -m venv --without-pip virtual```
* Activate the virtual environment using 
    ```$ source virtual/bin/activate```
* Download pip in our environment using 
    ```$ curl https://bootstrap.pypa.io/get-pip.py | python```
* Install all the dependencies from the requirements.txt file by running 
    ```python3.6 pip install -r requirements.txt```
* Add a secret_key, mail_username and mail_password to your environment. In a folder named instance, file named config.py

* (optional) Create a `start.sh` to easily run the app:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

        python3 manage.py server

* Make the start.sh an executable by changing permissions:

        $ chmod a+x start.sh

* Start the app using:
        $ ./start.sh

* In the config.py choose which mode to run your app(use development or test at first)
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py test
        
## Technologies Used
* Python3.6
* Flask


## Developed by
Mutugi Mutuma

### License

MIT License
[MIT License](https://github.com/Mutugiii/Microblog/blob/master/LICENSE)