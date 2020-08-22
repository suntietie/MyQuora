# MyQuora: website to get knowledge
Source Code for MyQuora - A Q&A website
## What tools do you use?
### Backend
django / django-REST-framework, SQLite
### Frontend
Vue.js, django-crispy-forms
## Main Features
* User Login / Logout with one-step Authentication
* Ask / Edit / Delete Questions
* Write / Edit / Delete Answers
* Like / Unlike single answer 
* Render Newly Posted Questions / Answer first
## How do I try this website?
This website hasn't deployed to server yet, but you could ```git clone``` and play it locally.

* Firstly try ```cd MyQuora```
* Create python virtual environment
  
  ```bash
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r ./requirements.txt
  ```
* Run migration is essential to Django
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
* Then come to the frontend - Vue.js
  ```bash
    cd QuestionTime/frontend
    npm install
  ```
* Run Vue and Django server in different terminals
  ```bash
    npm run serve
    python manage.py runserver
  ```
* Open 127.0.0.1:8000 on Chrome to enjoy this website!
## Photos

![HomePage](/images/HomePage.png)

![LoginPage](/images/LoginPage.png)

![QuestionPage](/images/QuestionPage.png)