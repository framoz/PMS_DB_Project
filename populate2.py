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

# Helper function to get a random ID from a table
def get_random_id(table_name, id_column):
    """Fetch a random ID from a given table and column."""
    cursor.execute(f"SELECT {id_column} FROM {table_name}")
    ids = cursor.fetchall()
    if ids:
        return random.choice(ids)[0]
    else:
        return None

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

def populate_product_sale():
    """Populate ProductSale with random data."""
    for _ in range(10):
        id_product = get_random_id("Product", "IDProduct")
        id_sale = get_random_id("Sale", "IDSale")
        quantity = random.randint(1, 10)

        if id_product and id_sale:
            cursor.execute("""
                INSERT INTO ProductSale (IDProduct, IDSale, Quantity)
                VALUES (?, ?, ?)
            """, (id_product, id_sale, quantity))

def populate_invoice_sale():
    """Populate InvoiceSale with random data."""
    for _ in range(5):
        id_invoice = get_random_id("Invoice", "IDInvoice")
        id_sale = get_random_id("Sale", "IDSale")
        if id_invoice and id_sale:
            cursor.execute("""
                INSERT INTO InvoiceSale (IDInvoice, IDSale)
                VALUES (?, ?)
            """, (id_invoice, id_sale))

def populate_product():
    for _ in range(20):  # Add 20 products
        name = fake.word().capitalize() + " " + fake.word().capitalize()
        price = round(random.uniform(10, 1000), 2)
        department_id = get_random_id("Department", "IDDepartment")
        
        if department_id:
            cursor.execute("INSERT INTO Product (Name, Price, IDDepartment) VALUES (?, ?, ?)", 
                           (name, price, department_id))
def populate_sale():
    for _ in range(30):  # Add 30 sales
        sale_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
        amount = round(random.uniform(100, 10000), 2)
        contact_id = get_random_id("Contact", "IDContact")
        project_id = get_random_id("Project", "IDProject")

        if contact_id and project_id:
            cursor.execute("INSERT INTO Sale (Date, Amount, IDContact, IDProject) VALUES (?, ?, ?, ?)", 
                           (sale_date, amount, contact_id, project_id))
# def populate_invoice_sale():
#     for _ in range(5):  # Add 5 invoice-sale connections
#         invoice_id = get_random_id("Invoice", "IDInvoice")
#         sale_id = get_random_id("Sale", "IDSale")
        
#         if invoice_id and sale_id:
#             cursor.execute("INSERT INTO InvoiceSale (IDInvoice, IDSale) VALUES (?, ?)", 
#                            (invoice_id, sale_id))

def populate_invoice_sale():
    for _ in range(5):  # Add 5 invoice-sale connections
        invoice_id = get_random_id("Invoice", "IDInvoice")
        sale_id = get_random_id("Sale", "IDSale")

        # Ensure no duplicate IDInvoice or IDSale pair exists
        cursor.execute("""
            SELECT 1 FROM InvoiceSale WHERE IDInvoice = ? AND IDSale = ?
        """, (invoice_id, sale_id))
        existing_entry = cursor.fetchone()

        if not existing_entry:  # Only insert if no matching pair exists
            cursor.execute("INSERT INTO InvoiceSale (IDInvoice, IDSale) VALUES (?, ?)", 
                           (invoice_id, sale_id))
        else:              
            print(f"Skipping duplicate entry for Invoice {invoice_id} and Sale {sale_id}")

def populate_product_sale():
    for _ in range(10):  # Add 10 product-sale connections
        product_id = get_random_id("Product", "IDProduct")
        sale_id = get_random_id("Sale", "IDSale")
        quantity = random.randint(1, 10)

        if product_id and sale_id:
            cursor.execute("""
                INSERT INTO ProductSale (IDProduct, IDSale, Quantity)
                VALUES (?, ?, ?)
            """, (product_id, sale_id, quantity))

def populate_employee_department():
    for employee_id in range(17,51):  # Add 15 employee-department connections
        ##employee_id = get_random_id("Employee", "IDEmployee")
        department_id = get_random_id("Department", "IDDepartment")
        dep_title = fake.job()

        if employee_id and department_id:
            cursor.execute("""
                INSERT INTO EmployeeDepartment (IDEmployee, IDDepartment, DepTitle)
                VALUES (?, ?, ?)
            """, (employee_id, department_id, dep_title))

def populate_invoice():
    for _ in range(10):  # Add 10 invoices
        invoice_date = random_date(datetime(2020, 1, 1), datetime(2023, 1, 1))
        total_amount = round(random.uniform(100, 5000), 2)
        currency_id = get_random_id("Currency", "IDCurrency")
        company_id = get_random_id("Company", "IDCompany")
        contact_id = get_random_id("Contact", "IDContact")

        if currency_id:
            cursor.execute("INSERT INTO Invoice (InvoiceDate, TotalAmount, IDCurrency, IDCompany, IDContact) VALUES (?, ?, ?, ?, ?)",
                           (invoice_date, total_amount, currency_id,company_id, contact_id ))

def populate_employee():
    for employee_id in range(17, 51):
        
        id_role = get_random_id("Role", "IDRole")
        work_since = random_date(datetime(2020, 1, 1), datetime(2023,1,1))
        contract_end = random_date(datetime(2023,2,2), datetime(2028, 1,1))
        salary = round(random.uniform(851,5000), 2)
        tax_id = fake.ein()[:18]
        id_company = get_random_id("Company", "IDCompany")

        

        if employee_id:
            cursor.execute("INSERT INTO Employee(IDEmployee, IDRole, WorkSince, ContractEnd, Salary, TaxID, IDCompany) VALUES (?,?,?,?,?,?,?)",
                           (employee_id, id_role, work_since, contract_end, salary, tax_id, id_company))
        
        
def populate_purchase():
    for _ in range(10):
        date = random_date(datetime(2020,1, 1), datetime(2023,1,1))
        amount = round(random.uniform(1, 99999))
        description = fake.sentence(20, True)
        id_company = get_random_id("Company", "IDCompany")
        id_partner = get_random_id("BusinessPartner", "IDPartner")
        id_currency = get_random_id("Currency", "IDCurrency")

        cursor.execute("INSERT INTO Purchase(Date, Amount, Description, IDCompany, IDPartner, IDCurrency) VALUES (?,?,?,?,?,?)",
                       (date, amount, description, id_company, id_partner, id_currency))

# Populate all tables
def populate_tables():
    populate_person()
    populate_business_partner()
    populate_role()
    populate_company()
    populate_currency()
    populate_department()
    populate_purchase()
    populate_employee()
    populate_contact()
    populate_invoice()  # Populating Invoice table
    populate_project()
    populate_employee_department()  # Populating EmployeeDepartment table
    populate_sale()
    populate_product()  # Populating Product table
    populate_invoice_sale()  # Populating InvoiceSale table
    populate_product_sale()  # Populating ProductSale table
    conn.commit()


# Execute the script
populate_tables()

# Close the connection
conn.close()
print("Database populated successfully!")
