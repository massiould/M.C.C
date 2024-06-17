# Avocat app

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:massiould/M.C.C.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv ~/.virtualenvs/djangodev
$ source ~/.virtualenvs/djangodev/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirement.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

```sh
(env)$ pip freeze >  requirement.txt
```
to add all new_packages in the requirement.txt

Once `pip` has finished downloading the dependencies:
```sh

(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/login/`.


```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
When you add new table make them appear by doing this.


```sh
(env)$ http://localhost:8000/admin/
(env)$ http://localhost:8000/choose-category/
(env)$ http://localhost:8000/login/
(env)$ http://localhost:8000/signup/


```

