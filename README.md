# Voucher - Django REST Framework

## How to run
### Enable Virtual Environment and Install the packages from docs/requirements.txt
> source venv/bin/activate

> pip install -r docs/requirements.txt

### Set PYTHONPATH and run the server
> cd $HOME/\<project-dir\>

> (export PYTHONPATH='$HOME/\<project-dir\>' && python3 api/manage.py runserver)

## URLS
> 'localhost/' -> Hello World page (Landing page)

> 'localhost/voucher/' -> Redeem Voucher Page

> 'localhost/get-vouchers/' -> GET all vouchers

> 'localhost/get-voucher/\<id\>' -> GET a voucher by ID