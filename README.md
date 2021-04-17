# Users
redixdemo
create venv :
python3 -m venv venv
activate it by:
source venv/bin/activate
in this app you can register user,generate auth token,filter and search users.
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
cd Users
and run ./manage.py migrate && ./manage.py runserver
you will find api url endpoints on : localhost:8000 
