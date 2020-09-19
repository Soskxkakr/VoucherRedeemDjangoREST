# Voucher - Django REST Framework

## How to run
### Enable Virtual Environment and Install the packages from docs/requirements.txt
> source venv/bin/activate

> pip install -r docs/requirements.txt

### Set PYTHONPATH and run the server
> cd $HOME/\<project-dir\>

> (export PYTHONPATH='$HOME/\<project-dir\>' && python3 api/manage.py runserver)

## URLS
> 'localhost/' -> Redeem Voucher Page

> 'localhost/get-vouchers/' -> GET all vouchers

> 'localhost/get-voucher/\<id\>' -> GET a voucher by ID

> 'localhost/add-voucher/' -> ADD(PUT/POST) a new voucher

> 'localhost/update-voucher/\<id\>' UPDATE a voucher by ID

> 'localhost/delete-vouucher/\<id\>' DELETE a voucher by ID (METHOD NOT ALLOWED)

> 'localhost/site-admin/' -> Admin Site to POST/PUT/PATCH/DELETE a voucher

## Voucher Model / Object
```
{
    "voucher_code" : <code>,
    "discount" : <discount value>,
    "no_of_use" : <number of use>
}
```

## Guides
1. Check Voucher's availability and code from /localhost/get-vouchers
2. If voucher's "number of use" is 0, edit it through the /localhost/update-voucher/ or /localhost/site-admin/ page
3. Redeem the voucher again through /localhost/voucher/