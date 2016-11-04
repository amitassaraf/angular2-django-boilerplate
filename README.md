# cookiecutter-angular2-django

Overview 
===
This is a flexiable boilerplate for Angular 2 and Django.
It also uses cookiecutter.

This repository is a merge of a django boilerplate and @AngularClass's angular2-webpack-starter.

Quickstart
===

To begin:

Either use -

```bash
cookiecutter gh:amitassaraf/angular2-django-boilerplate
```

or 

```bash
git clone https://github.com/amitassaraf/angular2-django-boilerplate 

cd angular2-django-boilerplate

cookiecutter .
```

Then fill in all the information asked.

If you don't have cookie cutter, install it using:
```bash
npm install cookiecutter -g
```

Frontend
-----
-----

After running cookiecutter, enter yourappname/src/frontend
and run:
```bash
sudo npm install
```

Then run:
```bash
npm start
```
To start the development web pack server and make sure everything is working good.

at this point you can surf to http://localhost:3000 to see the boilerplate front end website.

Backend
---
-----

Install all the requirements:
```bash
pip install -r requirements.txt
```

Create the Django DB:
```bash
createdb {{cookiecutter.app_name}}
```

Migrate the database and create a superuser:
```bash
python {{cookiecutter.app_name}}/manage.py migrate
python {{cookiecutter.app_name}}/manage.py createsuperuser
```

Start the development server:
```bash
python {{cookiecutter.app_name}}/manage.py runserver
```

Contact Me
---
---
If you have any problems/suggestions you can always contact me

**Email**: amitassaraf@me.com
**Website**: http://amitassaraf.com