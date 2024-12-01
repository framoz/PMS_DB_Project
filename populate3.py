import random
import faker
from datetime import datetime, timedelta

# Initialize Faker for realistic data generation
fake = faker.Faker()

# Output SQL file
output_file = '/home/framoz/DataGripProjects/401_DB_Proj/populate2.sql'

# Helper function to generate random dates
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Helper function to write SQL statements to a file
def write_to_file(statement):
    with open(output_file, 'a') as f:
        f.write(statement + ';\n')

# Generate and insert data as SQL statements
def populate_currency():
    currencies = ['USD', 'EUR', 'GBP']
    for currency in currencies:
        write_to_file(f"INSERT INTO Currency (CurrencyName) VALUES ('{currency}')")

def populate_company():
    for _ in range(10):  # Add 10 companies
        name = fake.company().replace("'", "''")
        address = fake.address().replace("'", "''")
        email = fake.company_email().replace("'", "''")
        phone = fake.phone_number().replace("'", "''")
        write_to_file(f"INSERT INTO Company (Name, Address, Email, Phone) VALUES ('{name}', '{address}', '{email}', '{phone}')")

def populate_business_partner():
    for _ in range(15):  # Add 15 business partners
        name = fake.name().replace("'", "''")
        tax_id = fake.ein()[:14]
        address = fake.address().replace("'", "''")
        write_to_file(f"INSERT INTO BusinessPartner (Name, TaxID, Address) VALUES ('{name}', '{tax_id}', '{address}')")

def populate_department():
    for _ in range(15):  # Add 15 departments
        name = fake.bs().capitalize().replace("'", "''")
        budget = round(random.uniform(10000, 100000), 2)
        phone = fake.phone_number().replace("'", "''")
        email = fake.company_email().replace("'", "''")
        company_id = random.randint(1, 10)
        write_to_file(f"INSERT INTO Department (Name, Budget, Phone, Email, IDCompany) VALUES ('{name}', {budget}, '{phone}', '{email}', {company_id})")

def populate_person():
    for person_id in range(1, 51):  # Add 50 persons
        name = fake.first_name().replace("'", "''")
        surname = fake.last_name().replace("'", "''")
        gender = random.choice(['Male', 'Female', 'Other'])
        birthdate = random_date(datetime(1970, 1, 1), datetime(2000, 1, 1))
        address = fake.address().replace("'", "''")
        phone = fake.phone_number().replace("'", "''")
        email = fake.email().replace("'", "''")
        write_to_file(f"INSERT INTO Person (IDPerson, Name, Surname, Gender, Birthdate, Address, Phone, Email) VALUES ({person_id}, '{name}', '{surname}', '{gender}', '{birthdate}', '{address}', '{phone}', '{email}')")

def populate_employee():
    for employee_id in range(1, 51):  # Make each person an employee
        role_id = random.randint(1, 10)
        work_since = random_date(datetime(2010, 1, 1), datetime(2020, 1, 1))
        contract_end = random_date(datetime(2021, 1, 1), datetime(2030, 1, 1))
        salary = round(random.uniform(1000, 10000), 2)
        tax_id = fake.ein()[:14].replace("'", "''")
        company_id = random.randint(1, 10)
        write_to_file(f"INSERT INTO Employee (IDEmployee, IDRole, WorkSince, ContractEnd, Salary, TaxID, IDCompany) VALUES ({employee_id}, {role_id}, '{work_since}', '{contract_end}', {salary}, '{tax_id}', {company_id})")

# Populate all tables
def populate_tables():
    with open(output_file, 'w') as f:
        f.write("-- SQL Script to populate the database\n")

    populate_currency()
    populate_company()
    populate_business_partner()
    populate_department()
    populate_person()
    populate_employee()

# Execute the script
populate_tables()
print("SQL file generated successfully!")
