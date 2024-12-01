PRAGMA foreign_keys = ON;

--DROP TABLE IF EXISTS BusinessPartner;
--DROP TABLE IF EXISTS Invoice;
--DROP TABLE IF EXISTS Product;
--DROP TABLE IF EXISTS ProductSale;
--DROP TABLE IF EXISTS InvoiceSale;
--DROP TABLE IF EXISTS Sale;

--DROP TABLE IF EXISTS Contact;
--DROP TABLE IF EXISTS Employee;
--DROP TABLE IF EXISTS Person;
--DROP TABLE IF EXISTS Role;
--DROP TABLE IF EXISTS EmployeeDepartment;
--DROP TABLE IF EXISTS Department;
--DROP TABLE IF EXISTS Project;
--DROP TABLE IF EXISTS Currency;
--DROP TABLE IF EXISTS Purchase;
--DROP TABLE IF EXISTS Company;

DROP TABLE IF EXISTS ProductSale;
DROP TABLE IF EXISTS InvoiceSale;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Sale;
DROP TABLE IF EXISTS EmployeeDepartment;
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Invoice;
DROP TABLE IF EXISTS Contact;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Purchase;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Currency;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS BusinessPartner;
DROP TABLE IF EXISTS Person;

-- Table: BusinessPartner
CREATE TABLE BusinessPartner (
                                 IDPartner INTEGER PRIMARY KEY AUTOINCREMENT,
                                 Name VARCHAR(255) NOT NULL,
                                 TaxID VARCHAR(18) NOT NULL UNIQUE, -- Chinese taxid has 18 chars
                                 Address TEXT
);

-- Table: Invoice
CREATE TABLE Invoice (
                         IDInvoice INTEGER PRIMARY KEY AUTOINCREMENT ,
                         InvoiceDate DATE NOT NULL,
                         TotalAmount DECIMAL NOT NULL,
                         IDCurrency INTEGER NOT NULL,
                         IDCompany INTEGER NOT NULL,
                         IDContact INTEGER NOT NULL,
                         FOREIGN KEY (IDCurrency) REFERENCES Currency(IDCurrency),
                         FOREIGN KEY (IDCompany) REFERENCES Company(IDCompany),
                         FOREIGN KEY (IDContact) REFERENCES Contact(IDContact)
);

-- Table: Product
CREATE TABLE Product (
                         IDProduct INTEGER PRIMARY KEY AUTOINCREMENT ,
                         Name VARCHAR(255) NOT NULL UNIQUE,
                         Price DECIMAL NOT NULL,
                         IDDepartment INTEGER NOT NULL,
                         FOREIGN KEY (IDDepartment) REFERENCES Department(IDDepartment)
);

-- Table: ProductSale (many to many)
CREATE TABLE ProductSale (
                        IDProduct INTEGER NOT NULL,
                        IDSale INTEGER NOT NULL,
                        Quantity INTEGER NOT NULL,
                        PRIMARY KEY (IDProduct, IDSale),
                        FOREIGN KEY (IDProduct) REFERENCES Product(IDProduct),
                        FOREIGN KEY (IDSale) REFERENCES Sale(IDSale)
);

CREATE TABLE InvoiceSale (
                             IDInvoice INTEGER PRIMARY KEY,
                             IDSale INTEGER NOT NULL UNIQUE,                            
                             FOREIGN KEY (IDInvoice) REFERENCES Invoice(IDInvoice),
                             FOREIGN KEY (IDSale) REFERENCES Sale(IDSale)
);

CREATE TABLE Sale (
                      IDSale INTEGER PRIMARY KEY AUTOINCREMENT ,
                      Date DATE NOT NULL,
                      Amount DECIMAL NOT NULL,
                      IDContact INTEGER NOT NULL,
                      IDProject INTEGER NOT NULL,
                      FOREIGN KEY (IDContact) REFERENCES Contact(IDContact),
                      FOREIGN KEY (IDProject) REFERENCES Project(IDProject)
);

CREATE TABLE Company (
                         IDCompany INTEGER PRIMARY KEY AUTOINCREMENT,
                         Name VARCHAR(255) NOT NULL UNIQUE,
                         Address TEXT NOT NULL,
                         Email TEXT NOT NULL UNIQUE CHECK (email LIKE '%_@__%.__%'),
                         Phone VARCHAR(20),
                         UNIQUE (Name, Address)
);


CREATE TABLE Person (
                        IDPerson INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL,
                        Surname TEXT NOT NULL,
                        Gender TEXT CHECK (Gender IN ('Male', 'Female', 'Other')),
                        Birthdate DATE NOT NULL,
                        Address TEXT,
                        Phone VARCHAR(20),
                        Email VARCHAR(255) NOT NULL UNIQUE CHECK (Email LIKE '%_@_%._%')


);


CREATE TABLE Employee (
                          IDEmployee INTEGER PRIMARY KEY,
                          IDRole INTEGER NOT NULL,
                          WorkSince DATE NOT NULL,
                          ContractEnd DATE CHECK (ContractEnd > WorkSince),
                          Salary DECIMAL NOT NULL CHECK ( Salary > 850 ),
                          TaxID VARCHAR(18) NOT NULL UNIQUE, --18 because in China it has 18 characters
                          IDCompany INTEGER NOT NULL,
                          FOREIGN KEY (IDRole) REFERENCES Role(IDRole) ON DELETE CASCADE,
                          FOREIGN KEY (IDEmployee) REFERENCES Person(IDPerson),
                          FOREIGN KEY (IDCompany) REFERENCES Company(IDCompany)
);

CREATE TABLE Contact (
                         IDContact INTEGER PRIMARY KEY,
                         JobDescription TEXT,
                         IDPartner INTEGER NOT NULL,
                         FOREIGN KEY (IDContact) REFERENCES Person(IDPerson) ON DELETE CASCADE,
                         FOREIGN KEY (IDPartner) REFERENCES BusinessPartner(IDPartner)
);

-- Table: Role
CREATE TABLE Role (
                      IDRole INTEGER PRIMARY KEY AUTOINCREMENT ,
                      Name VARCHAR(255) NOT NULL
);

-- Table: EmployeeDepartment
CREATE TABLE EmployeeDepartment (
                                    IDEmployee INTEGER NOT NULL UNIQUE,
                                    IDDepartment INTEGER NOT NULL,
                                    DepTitle VARCHAR(255),
                                    PRIMARY KEY (IDEmployee, IDDepartment),
                                    FOREIGN KEY (IDEmployee) REFERENCES Employee(IDEmployee),
                                    FOREIGN KEY (IDDepartment) REFERENCES Department(IDDepartment)
);

-- Table: Department
CREATE TABLE Department (
                            IDDepartment INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name VARCHAR(100) NOT NULL,
                            Budget DECIMAL,
                            Phone VARCHAR(255) UNIQUE ,
                            Email TEXT UNIQUE ,
                            IDCompany INTEGER NOT NULL,
                            FOREIGN KEY (IDCompany) REFERENCES Company(IDCompany)
);

-- Table: Project
CREATE TABLE Project (
                         IDProject INTEGER PRIMARY KEY AUTOINCREMENT,
                         Name VARCHAR(100) NOT NULL,
                         StartDate DATE NOT NULL,
                         EndDate DATE CHECK (EndDate > StartDate),
                         IDDepartment INTEGER NOT NULL,
                         FOREIGN KEY (IDDepartment) REFERENCES Department(IDDepartment)
);

-- Table: Currency
CREATE TABLE Currency (
                          IDCurrency INTEGER PRIMARY KEY AUTOINCREMENT,
                          CurrencyName VARCHAR(50) NOT NULL UNIQUE
);

-- Table: Purchase
CREATE TABLE Purchase (
                          IDPurchase INTEGER PRIMARY KEY AUTOINCREMENT,
                          Date DATE NOT NULL,
                          Amount DECIMAL NOT NULL,
                          Description TEXT,
                          IDCompany INTEGER NOT NULL,
                          IDPartner INTEGER NOT NULL,
                          IDCurrency INTEGER NOT NULL,
                          FOREIGN KEY (IDCompany) REFERENCES Company(IDCompany),
                          FOREIGN KEY (IDPartner) REFERENCES BusinessPartner(IDPartner),
                          FOREIGN KEY (IDCurrency) REFERENCES Currency(IDCurrency)
                      );

