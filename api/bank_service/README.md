# Bank System
## This project is a simple Bank system which is included 5 modeles:
###1- Bank
###2- Atm
###3- Customer
###4- Bank Branch
###5- Employee
## This project has 2 Endpoints:
### Transaction
```curl
curl --location --request POST 'http://127.0.0.1:8000/api/transaction/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bank_branch_id": 2,
    "operation": "card_to_card",
    "account_id": 1,
    "amount": 1000
}'
```
### Regiseration
```curl
curl --location --request POST 'http://127.0.0.1:8000/api/account/' \
--header 'Content-Type: application/json' \
--data-raw '{
 "bank_id": "2",
 "customer_id": "1",
 "bank_branch_id": "1"
}'
```
# Deployment 
## The first thing to do is to clone the repository:
$ git@github.com:RasoulKhosravi/Bank_system.git
$ cd bank-service

## Activate virtual environment:
$ source env/bin/activate

### Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv

- (env)$ cd project
- (env)$ python manage.py migrate 
- (env)$ python manage.py makemigrations
- (env)$ python manage.py createsuperuser
- (env)$ python manage.py runserver

# Create Models in admin 
## navigate to http://127.0.0.1:8000/admin
## Before you interact with the application, go to admin panel and make 5 models.

# Validation of registration

## The requested bank branch should be the same with the bank which is already registerd
## The requested bank branch must have an employee related to the account opening operation.

# Validation of Transaction 

## To perform withdrawals and deposits, the customer must have an account in one of the bank branches
## The bank branch requested must have an employee who is responsible for specifically requested operation such as withdrawal and deposits

