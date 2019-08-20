# Complaint system for NITC

## Setup:
1. git clone git@gitlab.com:farisshajahan/drugs-complaint-system.git
2. cd drugs-complaint-system
3. virtualenv -p $(which python3) venv 
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py runserver

The site should open up at localhost:8000
