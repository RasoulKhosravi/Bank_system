# Bank System made by Django 4.0.5
## This project is a simple Bank system which is included 5 modeles:
### 1- Bank
- Each bank has many bankbranchs.
### 2- Bank Branch
- Each bankbranch belonge to one bank
- Each bankbranch has many ATM's
- Each bankbranch has many employees
- Each bankbranch has many customers, through by account
### 3- Customer
- Each customer has many branches, through by account
### 4- Atm
- Each Atm belongs to one branch
### 5- Employee
- Each employee belongs to one branch
### 6- Transaction
- Each transaction belongs to one account
- Each transaction belongs to one branch
### 7- Account
- Each account belongs to one customer
- Each account belongs to one branch
##  This project has 2 Endpoints:

### Curl Sample to send and get request  
### Transaction, 
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
 "customer_id": "1",
 "bank_branch_id": "1"
}'
```
# Deployment
## The first thing to do is to clone the repository:
- git clone git@github.com:RasoulKhosravi/Bank_system.git
- cd Bank_system

## Activate virtual environment:
- source env/bin/activate

### Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

- (env)$ cd bank_service
- (env)$ python manage.py makemigrations // Packaging up your model changes into individual migration files
- (env)$ python manage.py migrate // Propagating changes you make to your models into your database schema
- (env)$ python manage.py createsuperuser // Create a super admin who has all permissions
- (env)$ python manage.py runserver // Run a server on your local machine 

## navigate to http://127.0.0.1:8000/admin
## Create dumy data for tables and CRUD for Bank, Bank Branch, ATM, Employee, Customer into admin panel 

# Set Validation logic for registration of customer
- Customer not allow to register into one branch at the time.
- The requested bank branch must have an employee related to the account opening operation.

# Set Validation logic for Transaction 

- To perform withdrawals and deposits, the customer must have an account in one of the bank branches.
- The bank branch requested must have an employee who is responsible for specifically requested operation such as withdrawal and deposits.
- To perform card-to-card operation, the customer must go to a branch that has an Atm at least.
