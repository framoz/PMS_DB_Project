import sqlite3
import random
import faker
from datetime import datetime, timedelta

# Initialize Faker for realistic data generation
fake = faker.Faker()

# Connect to SQLite database
conn = sqlite3.connect('/home/framoz/DataGripProjects/401_DB_Proj/identifier.sqlite')  # Replace with your database file
cursor = conn.cursor()

# Helper function to generate random dates
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Generate and insert data
def populate_currency():
    currencies = ['USD', 'EUR', 'GBP']
    for currency in currencies:
        cursor.execute("INSERT INTO Currency (CurrencyName) VALUES (?)", (currency,))

def populate_company():
    for _ in range(10):  # Add 10 companies
        name = fake.company()
        address = fake.address()
        email = fake.company_email()
        phone = fake.phone_number()
        cursor.execute("INSERT INTO Company (Name, Address, Email, Phone) VALUES (?, ?, ?, ?)", (name, address, email, phone))

def populate_business_partner():
    for _ in range(15):  # Add 15 business partners
        name = fake.name()
        tax_id = fake.ein()[:14]
        address = fake.address()
        cursor.execute("INSERT INTO BusinessPartner (Name, TaxID, Address) VALUES (?, ?, ?)", (name, tax_id, address))

def populate_department():
    for _ in range(15):  # Add 15 departments
        name = fake.bs().capitalize()
        budget = round(random.uniform(10000, 100000), 2)
        phone = fake.phone_number()
        email = fake.company_email()
        company_id = random.randint(1, 10)
        cursor.execute("INSERT INTO Department (Name, Budget, Phone, Email, IDCompany) VALUES (?, ?, ?, ?, ?)", 
                       (name, budget, phone, email, company_id))

def populate_person():
    for person_id in range(1, 51):  # Add 50 persons
        name = fake.first_name()
        surname = fake.last_name()
        gender = random.choice(['Male', 'Female', 'Other'])
        birthdate = random_date(datetime(1970, 1, 1), datetime(2000, 1, 1))
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()
        cursor.execute("INSERT INTO Person (IDPerson, Name, Surname, Gender, Birthdate, Address, Phone, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                       (person_id, name, surname, gender, birthdate, address, phone, email))

def populate_employee():
    for person_id in range(1, 51):  # Make each person an employee
        role_id = random.randint(1, 10)
        work_since = random_date(datetime(2010, 1, 1), datetime(2020, 1, 1))
        contract_end = random_date(datetime(2021, 1, 1), datetime(2030, 1, 1))
        salary = round(random.uniform(1000, 10000), 2)
        tax_id = fake.ein()[:14]
        company_id = random.randint(1, 10)
        cursor.execute("INSERT INTO Employee (IDEmployee, IDRole, WorkSince, ContractEnd, Salary, TaxID, IDCompany) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (person_id, role_id, work_since, contract_end, salary, tax_id, company_id))

def populate_role():
    roles = ['Manager', 'Engineer', 'Analyst', 'Technician', 'Clerk', 'Supervisor', 'Executive', 'Consultant', 'Director', 'Assistant']
    for role in roles:
        cursor.execute("INSERT INTO Role (Name) VALUES (?)", (role,))

def populate_project():
    for _ in range(20):  # Add 20 projects
        name = fake.bs().capitalize()
        start_date = random_date(datetime(2020, 1, 1), datetime(2022, 1, 1))
        end_date = random_date(datetime(2023, 1, 1), datetime(2025, 1, 1))
        department_id = random.randint(1, 15)
        cursor.execute("INSERT INTO Project (Name, StartDate, EndDate, IDDepartment) VALUES (?, ?, ?, ?)", 
                       (name, start_date, end_date, department_id))

def populate_sale():
    for _ in range(30):  # Add 30 sales
        sale_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
        amount = round(random.uniform(100, 10000), 2)
        contact_id = random.randint(1, 15)
        project_id = random.randint(1, 20)
        cursor.execute("INSERT INTO Sale (Date, Amount, IDContact, IDProject) VALUES (?, ?, ?, ?)", 
                       (sale_date, amount, contact_id, project_id))

def populate_contact():
    for contact_id in range(1, 16):  # Add 15 contacts
        job_description = fake.job()
        partner_id = random.randint(1, 15)
        cursor.execute("INSERT INTO Contact (IDContact, JobDescription, IDPartner) VALUES (?, ?, ?)", 
                       (contact_id, job_description, partner_id))

# Populate all tables
def populate_tables():
    populate_currency()
    populate_company()
    populate_business_partner()
    populate_department()
    populate_person()
    populate_employee()
    populate_role()
    populate_project()
    populate_sale()
    populate_contact()  # Added to populate Contact table
    conn.commit()

# Execute the script
populate_tables()

# Close the database connection
conn.close()
print("Database populated successfully!")
