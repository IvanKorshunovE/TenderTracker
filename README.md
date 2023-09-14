# Tender Display

**Username:** demo  
**Password:** demo

This application, built on Django, displays a list/table of tenders from a local database, which are at some point loaded via the API.

## Endpoints

1. **/** – The home page for non-authorized users contains a form for authorization (a demo user with a demo password is provided for a quick test). If the user is authorized, we transfer it to /tenders.
2. **/tenders** – (only available to authorized users) displays a list/table of tenders from a local database that have been loaded via the API at some point.

## Installing / Getting started

A brief overview of the minimum configuration required to run this application.

```shell
git clone https://github.com/IvanKorshunovE/TenderTracker
cd TenderTracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Create an .env file, fill in its contents
python manage.py make_setup
python manage.py fetch_tenders
```

After running these commands, the Django server should be up and running, allowing you to access and interact with the application.
