[![CircleCI](https://circleci.com/gh/daisyndungu/cp2-BucketList-Application/tree/backend.svg?style=svg)](https://circleci.com/gh/daisyndungu/cp2-BucketList-Application/tree/backend) [![Coverage Status](https://coveralls.io/repos/github/daisyndungu/cp2-BucketList-Application/badge.svg?branch=backend)](https://coveralls.io/github/daisyndungu/cp2-BucketList-Application?branch=backend) [![Code Health](https://landscape.io/github/daisyndungu/cp2-BucketList-Application/backend/landscape.svg?style=flat)](https://landscape.io/github/daisyndungu/cp2-BucketList-Application/backend)


# cp2-BucketList-Application
Online Bucket List service using Flask.(RESTful API)

The building blocks are:
  * Flask Restful
  * SQLalchemy
  * Postgres (Database)

EndPoint | Functionality
------------ | -------------
POST /auth/login | Logs a user in and generates a unique token
POST /auth/register | Register a user
POST /bucketlists/  | Create a new bucket list
GET /bucketlists/ | List all the created bucket lists that belongs to the logged in user
GET /bucketlists/<id> | Get single bucket list
PUT /bucketlists/<id> | Updates the specified bucket list
DELETE /bucketlists/<id> | Delete the specified bucket list
POST /bucketlists/<id>/items/ | Create a new item in bucket list
PUT /bucketlists/<id>/items/<item_id> | Update a bucket list item
DELETE /bucketlists/<id>/items/<item_id> | Delete an item in a bucket list

## INSTALLATION

These are the basic steps to install and run the application locally.

* prepare directory for project code and virtualenv:

      $ mkdir -p ~/bucketlist

      $ cd ~/bucketlist
* prepare virtual environment (with virtualenv you get pip, we'll use it soon to install requirements):

      $ virtualenv --python=python3 bucketlist-venv

      $ source bucketlist-venv/bin/activate
* Clone the application:

      $ git clone https://github.com/daisyndungu/cp2-BucketList-Application.git

* install requirements into virtualenv:

      $ pip install -r cp2-BucketList-Application/requirements.txt
      $ git checkout backend
 * Start the application. This will initialize the database and create tables.

       $ python manage.py db init
       $ python manage.py db migrate
       $ python manage.py db upgrade
   
 * Run server

       $ python manage.py db runserver
       
