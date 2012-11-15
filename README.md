Flask-Skeleton
==============

This is a framework of a Flask application that can be run with gunicorn.  It incorporates the [recommended Flask pattern for larger applications](http://flask.pocoo.org/docs/patterns/packages/) and [wrapper classes for use with gunicorn and Flask](http://damianzaremba.co.uk/2012/08/running-a-wsgi-app-via-gunicorn-from-python/).

Requirements
------------

* Python 2.6-2.7
* virtualenv
* foreman (if you run the app with Procfile)

While not required, [autoenv](https://github.com/kennethreitz/autoenv) is really nice to have.


Getting Started
---------------

(1) Grab latest repo:

    git clone git://github.com/soccermetrics/flask-skeleton.git
    
(2) Set up your virtual environment:

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    
(3) Create a `.env` file and add the following line:

    export DEBUG=1

    
Usage
-----

If you're using Foreman, running the app is simple:

    $ foreman start
    
If you're not using Foreman, running the app is also simple:

    $ python appname/app.py

    
Changing appname
----------------

If you wish to change `appname`, you'll need to do so at the following places:

* both subdirectory names
* the MyCustomApplication import in `runserver.py`
* the `import_app()` call within the `load()` routine in `customapplication.py`

Deployment
----------

To deploy this app in Heroku:

    $ heroku create
    $ heroku config:add DEBUG=0
    $ git push heroku master
    
You'll have to tweak the code to deploy it on other platforms.


TODO
----

* Write a script to switch `appname` to whatever name I wish.


License
-------

This framework was created by [Howard Hamilton](http://github.com/howardhamilton). 
(c) 2012 [Soccermetrics Research, LLC](http://www.soccermetrics.net).

Everything is presented as-is without any warranty. Distributed via MIT license.

