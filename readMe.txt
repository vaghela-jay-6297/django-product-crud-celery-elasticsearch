Task:
-----
- create product model with name, description,size,capacity, color, price, quantity, image(upload multiple images) field.
- perform CRUD operation.
- when user insert/update/delete record at that time also record insert/update/delete in elastic search using Celery
- user can perform seach operation on name, description,size,capacity, color field using elastic search not data getting from DB.


Used Tools:
----------
- python
- django
- elastic search engine
- docker
- redis (celery)
- git
- postman - API testing collection


Project Structure:
-------------------
/project_folder
├── /DRF_elastic_celery_pro
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── /media
├── /product_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── documents.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── readMe.txt
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── .env
└── .env.format


Elastic Search setup:
---------------------
- create model into models.py then makemigrate and migrate it.
- install elastic search lib = "django-elasticsearch-dsl".
- register in installed app of settings.py file.
- create document.py file and add model and field with elastic search settings.
- build index in elasticsearch using "python manage.py search_index --rebuild". 
Note: elasticsearch engine is running. (in this project i user docker image of elastic search so start docker "docker compose up")


celery to auto insert, update, delete, search in elastic search:
----------------------------------------------------------------
- install celery package "pip install celery" and also install redis/rabbit server using "brew install redis" or "brew install rabbitmq".
- start redis/rabbit server using "brew services start redis" or "brew services start rabbitmq".
- create celery.py file in project_folder
- add some configration in project_folder/__init__.py file
- add some configration related to celery into setting.py file 
- now check celery working or not using run celery "celery -A project_name worker -l info"
- create tasks.py file into django_app to execute tasks related to elastic search
- add specific created task to specific module/function into views.py file.
- run celery "celery -A project_name worker -l info"


Dockerfile:
-----------
- using dockerfile create docker image
- copy all files and folders into docker image.
- create entrypoint.sh file to run command and migrate models & generate index file into elastic search.

Docker-compose.yml file:
------------------------
- add all images which use in django such as postgresql, celery, redis, elastic search, kibana.
- use postgresql image with giving authentication & database in environment variable.
- use elastic search same like postgresql
- use kibana to see elastic search index & monitor ES.
- add redis server to use celery to execute anonymous task like add document into elastic search.


Run Project using local sysytem:
--------------------------------
- install redis/rabbit server and start server using "brew services start redis"
- install elastic search engine and kibana dashboard.
- first start elastic search engine then start kibana using goto elasticsearch folder & kibana folder.
        ES: cd elasticsearch-8.14.2/  and run -> ./bin/elasticsearch
        kibana: cd kibana-8.14.2/   and run -> ./bin/kibana
- run celery worker using "celery -A DRF_elastic_celery_pro worker -l info"
- now you can access elastic search and kibana at "http://localhost:9200" & "http://localhost:5601" to monitor ES.
- run "python manage.py makemigrations" to create migrations files.
- run "python manage.py migrate" to execute migrations file to make tables into DB.
- run "python manage.py search_index --rebuild" to create indexes into elastic search.
- now start django server using "python manage.py runserver" 
- now perform operatios.


Run Project using Docker:
--------------------------
- install docker desktop and start docker application.
- build your docker compose file using "docker compose build".
- run your project using "docker compose up".
