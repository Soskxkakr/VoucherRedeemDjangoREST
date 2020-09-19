# Voucher - Django REST Framework

## How to run
### Install and Enable Virtual Environment and Install the packages from docs/requirements.txt
> python3 -m venv \<virtual env\>

> source venv/bin/activate

> pip install -r docs/requirements.txt

### Set PYTHONPATH, make migrations and run the server
> cd $HOME/\<project-dir\>

> python3 api/manage.py makemigrations

> python3 api/manage.py migrate

> (export PYTHONPATH='$HOME/\<project-dir\>' && python3 api/manage.py runserver)

### To have Admin Credentials
> python3 api/manage.py createsuperuser

Provide the details for the username, email, and password.
In this project its:
Username: *admin*
Password: *admin*

## URLS
> 'https://localhost:8000/' -> Redeem Voucher Page

> 'https://localhost:8000/get-vouchers/' -> GET all vouchers

> 'https://localhost:8000/get-voucher/\<id\>' -> GET a voucher by ID

> 'https://localhost:8000/add-voucher/' -> ADD(PUT/POST) a new voucher

> 'https://localhost:8000/update-voucher/\<id\>' UPDATE a voucher by ID

> 'https://localhost:8000/delete-vouucher/\<id\>' DELETE a voucher by ID (METHOD NOT ALLOWED)

> 'https://localhost:8000/site-admin/' -> Admin Site to POST/PUT/PATCH/DELETE a voucher

## Voucher Model / Object
```
{
    "voucher_code" : <code>,
    "discount" : <discount value>,
    "no_of_use" : <number of use>
}
```

## Guides
1. Check Voucher's availability and code from https://localhost:8000/get-vouchers
2. If voucher's "number of use" is 0, edit it through the https://localhost:8000/update-voucher/ or /localhost/site-admin/ page
3. Redeem the voucher again through https://localhost:8000/
