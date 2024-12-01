INSERT INTO BusinessPartner (Name, TaxID, Address) VALUES 
('Not a Client Co.', '123456789012345678', '123 General Exemplo Street, Porto'),
('Also Not a Fake Company ltd.', '987654321098765432', '122 A Street, Lisbon');

INSERT INTO Company (Name, Address, Email, Phone) VALUES 
('Super Company 1.', '456 Tech Park, Porto', 'info@sc1.com', '+351123456789'),
('Lesser Super Company', '789 Logistics Ave, Lisbon', 'contact@lsc.com', '+351987654321');

INSERT INTO Currency (CurrencyName) VALUES 
('Euro'),
('US Dollar');

INSERT INTO Department (Name, Budget, Phone, Email, IDCompany) VALUES 
('Development', 1000000, '+3511122334455', 'dev@company.com', 1),
('Sales', 500000, '+3516677889900', 'sales@company.com', 2);

INSERT INTO Project (Name, StartDate, EndDate, IDDepartment) VALUES 
('Important Project 1', '2024-01-15', '2024-12-31', 1),
('Another Project etc etc', '2024-02-01', '2024-08-01', 2);

INSERT INTO Person (Name, Surname, Gender, Birthdate, Address, Phone, Email) VALUES 
('Felipe', 'Ramos', 'Male', '2001-05-22', 'Abcde Street, Porto', '+3519988776655', 'felipe@felipe.com'),
('Felipa', 'Ramos', 'Female', '2001-1-1', '123, Travessa A Street, Lisboa', '+3518899776655', 'email@email.com');

INSERT INTO Role (Name) VALUES 
('Software Engineer'),
('Sales Manager');

INSERT INTO Employee (IDEmployee, IDRole, WorkSince, ContractEnd, Salary, TaxID, IDCompany) VALUES 
(1, 1, '2020-03-15', '2025-03-15', 1500, '123456789012345678', 1),
(2, 2, '2021-07-01', NULL, 2000, '987654321098765432', 2);

INSERT INTO EmployeeDepartment (IDEmployee, IDDepartment, DepTitle) VALUES 
(1, 1, 'Developer'),
(2, 2, 'Regional Sales');

INSERT INTO Contact (IDContact, JobDescription, IDPartner) VALUES 
(1, 'Software Vendor Contact', 1),
(2, 'Logistics Partner Contact', 2);

INSERT INTO Sale (Date, Amount, IDContact, IDProject) VALUES 
('2024-10-15', 1500, 1, 1),
('2024-11-20', 3000, 2, 2);

INSERT INTO Product (Name, Price, IDDepartment) VALUES 
('AI Software License', 5000, 1),
('Marketing Consulting Package', 2000, 2);

INSERT INTO ProductSale (IDProduct, IDSale, Quantity) VALUES 
(1, 1, 1),
(2, 2, 2);

INSERT INTO Invoice (InvoiceDate, TotalAmount, IDCurrency, IDCompany, IDContact) VALUES 
('2024-10-16', 1500, 1, 1, 1),
('2024-11-21', 6000, 1, 2, 2);

INSERT INTO InvoiceSale (IDInvoice, IDSale) VALUES 
(1, 1),
(2, 2);

INSERT INTO Purchase (Date, Amount, Description, IDCompany, IDPartner, IDCurrency) VALUES 
('2024-09-05', 800, 'Office Supplies', 1, 2, 1),
('2024-09-10', 1500, 'Software License', 2, 1, 1);
