# Code Louisville Python 2021 project by Virginia Swift 

This is a basic Django project integrated with Bootstrap, showcasing my concert photography (as I like to say, 
I'm not a pro, just a fan with a smartphone)

## INSTRUCTIONS

Create a project directory and install a python virtual environment inside it

```bash
mkdir project && cd project
python -m venv venv
source venv/bin/activate (for Windows it's venv\Scripts\activate)
```

Create a source dir and clone the repository

```bash
mkdir src && cd src
git clone https://github.com/vswift76/Kungen.git . 
```

Install the dependencies

```bash
pip install -r requirements/local.txt
```

Run the migrations and start the server!

```bash
python manage.py migrate
python manage.py runserver
```

SUCCESS! Go to `http://127.0.0.1:8000` to view my app :)


## PROJECT FEATURES LIST

```bash
Read and parse external file venues.json and display data
(COVID SUCKS past and upcoming concerts table)

Calculate and display data based on an external factor 
(ex: get the current date, and display how many days remaining until some event)
(Countdown to LTL 2021) 

Connect to an external/3rd party API and read data into your app
(Clicking on Flickr Gallery button takes you to a separate page of just a few of my photo galleries) 
```

## CREDITS

```bash
Basic Bootstrap template https://websitesetup.org/bootstrap-tutorial-for-beginners/ 
Flickr Gallery styled with nanogallery2 https://nanogallery2.nanostudio.org/
Django + Bootstrap Basic Setup from https://dev.to/thalesbruno/django-bootstrap-basic-setup-5dmb
```
