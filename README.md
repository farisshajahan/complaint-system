# Complaint system for NITC

## Setup:
1. git clone git@gitlab.com:farisshajahan/drugs-complaint-system.git
2. cd drugs-complaint-system
3. virtualenv -p $(which python3) venv 
4. source venv/bin/activate
5. pip install -r requirements.txt
6. cd complaint\_system && cp my.cnf.example my.cnf
7. Open my.cnf and fill it with you MYSQL connection parameters and the correct database
8. cd ../notifyapp && cp config.ini.example config.ini
9. Open config.ini and fill with correct details
10. Open the file mailinglist and fill it with emails to notify on separate lines
11. cd ../ && python manage.py migrate
12. python manage.py runserver

The site should open up at localhost:8000
