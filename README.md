## Simple CRM with Django Rest Framework

The purpose of the project is to show an implementation of Django Rest Framework.
After Log In users can register new clients, contacts with them and new orders.

### Technology Stack

* Django
* Django Rest Framework

### Installation

Create a folder, clone from Github, install dependencies and run a server
```
mkdir restcrm
cd restcrm
git clone https://github.com/Bounty1993/rest-crm.git
cd rest-crm
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Check it out
```
http://localhost:8000/accounts
```
### Project is under development