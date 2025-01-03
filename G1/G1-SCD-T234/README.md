# Requirement Document

## Title:  Group 1- G1-SCD-T234

## Group 1-  Customer, Orders, Products 

### 1. **Customers Table**
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(200)
);

-- Insert data
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
VALUES 
(1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', '456 Oak St'),
(3, 'Mary', 'Johnson', 'mary.johnson@example.com', '345-678-9012', '789 Pine St'),
(4, 'Michael', 'Brown', 'michael.brown@example.com', '456-789-0123', '101 Maple St'),
(5, 'David', 'Williams', 'david.williams@example.com', '567-890-1234', '202 Birch St'),
(6, 'Sarah', 'Jones', 'sarah.jones@example.com', '678-901-2345', '303 Cedar St'),
(7, 'Emily', 'Miller', 'emily.miller@example.com', '789-012-3456', '404 Ash St'),
(8, 'James', 'Davis', 'james.davis@example.com', '890-123-4567', '505 Redwood St'),
(9, 'Robert', 'Garcia', 'robert.garcia@example.com', '901-234-5678', '606 Fir St'),
(10, 'Linda', 'Martinez', 'linda.martinez@example.com', '012-345-6789', '707 Pine St');


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert data
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES 
(1, 1, '2024-01-15', 100.50),
(2, 2, '2024-02-10', 250.75),
(3, 3, '2024-03-05', 150.30),
(4, 4, '2024-04-20', 300.00),
(5, 5, '2024-05-10', 450.60),
(6, 6, '2024-06-01', 80.20),
(7, 7, '2024-07-13', 220.00),
(8, 8, '2024-08-25', 130.10),
(9, 9, '2024-09-17', 500.00),
(10, 10, '2024-10-22', 350.80);


CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

-- Insert data
INSERT INTO Products (ProductID, ProductName, Category, Price, StockQuantity)
VALUES 
(1, 'Laptop', 'Electronics', 999.99, 50),
(2, 'Smartphone', 'Electronics', 799.99, 100),
(3, 'Coffee Maker', 'Appliances', 49.99, 200),
(4, 'Headphones', 'Electronics', 129.99, 75),
(5, 'Desk Chair', 'Furniture', 149.99, 30),
(6, 'Tablet', 'Electronics', 499.99, 120),
(7, 'Blender', 'Appliances', 89.99, 150),
(8, 'Monitor', 'Electronics', 199.99, 60),
(9, 'Mouse', 'Accessories', 19.99, 300),
(10, 'Keyboard', 'Accessories', 49.99, 250);
```


## Title:  Group 2- G2-SCD-T234

## Group 2-  Suppliers, Categories, Employees 

### 1. **Suppliers Table**
```sql
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(100),
    ContactName VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(200)
);

-- Insert data
INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Phone, Address)
VALUES 
(1, 'Tech Supplies Inc.', 'Alice Cooper', '123-555-0101', '100 Tech Ave'),
(2, 'Home Appliances Co.', 'Bob Barker', '234-555-0202', '200 Appliance Rd'),
(3, 'Furniture World', 'Charlie Brown', '345-555-0303', '300 Furniture Blvd'),
(4, 'Gadget Central', 'David Lee', '456-555-0404', '400 Gadget St'),
(5, 'Office Essentials', 'Eva Green', '567-555-0505', '500 Office Park'),
(6, 'Smart Electronics', 'Frank White', '678-555-0606', '600 Electronics Pl'),
(7, 'Tech Gadgets Ltd.', 'Grace Hall', '789-555-0707', '700 Gadget Ln'),
(8, 'Blender Inc.', 'Hannah Scott', '890-555-0808', '800 Blend St'),
(9, 'Audio Tech', 'Ian Taylor', '901-555-0909', '900 Audio Dr'),
(10, 'Laptop Warehouse', 'Jack Carter', '012-555-1000', '1000 Laptop Rd');


CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50)
);

-- Insert data
INSERT INTO Categories (CategoryID, CategoryName)
VALUES 
(1, 'Electronics'),
(2, 'Appliances'),
(3, 'Furniture'),
(4, 'Accessories'),
(5, 'Clothing'),
(6, 'Books'),
(7, 'Food'),
(8, 'Toys'),
(9, 'Sports'),
(10, 'Beauty');

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Insert data
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(1, 'John', 'Adams', 'Sales', 55000.00),
(2, 'Emma', 'Clark', 'Marketing', 65000.00),
(3, 'Olivia', 'Taylor', 'HR', 60000.00),
(4, 'James', 'Davis', 'Engineering', 70000.00),
(5, 'Ava', 'Miller', 'Operations', 75000.00),
(6, 'Noah', 'Brown', 'IT', 80000.00),
(7, 'Liam', 'Wilson', 'Finance', 90000.00),
(8, 'Sophia', 'Moore', 'Sales', 45000.00),
(9, 'Lucas', 'Martin', 'Marketing', 48000.00),
(10, 'Mia', 'Lee', 'HR', 42000.00);

```


## Title:  Group 3- G2-SCD-T234

## Group 3-  Shippers , Payments , Invoices  

### 1. **Shippers Table**
```sql
CREATE TABLE Shippers (
    ShipperID INT PRIMARY KEY,
    ShipperName VARCHAR(100),
    Phone VARCHAR(20)
);

-- Insert data
INSERT INTO Shippers (ShipperID, ShipperName, Phone)
VALUES 
(1, 'FastShip', '123-555-1111'),
(2, 'Speedy Delivery', '234-555-2222'),
(3, 'Global Couriers', '345-555-3333'),
(4, 'QuickShip', '456-555-4444'),
(5, 'Cargo Express', '567-555-5555'),
(6, 'ShipFast', '678-555-6666'),
(7, 'Direct Freight', '789-555-7777'),
(8, 'Overnight Express', '890-555-8888'),
(9, 'ShipRight', '901-555-9999'),
(10, 'DeliverNow', '012-555-0000');

```
### 2. **Payments Table**
```sql
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    PaymentDate DATE,
    Amount DECIMAL(10, 2),
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert data
INSERT INTO Payments (PaymentID, OrderID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, 1, '2024-01-16', 100.50, 'Credit Card'),
(2, 2, '2024-02-11', 250.75, 'Debit Card'),
(3, 3, '2024-03-06', 150.30, 'PayPal'),
(4, 4, '2024-04-21', 300.00, 'Credit Card'),
(5, 5, '2024-05-11', 450.60, 'Cash'),
(6, 6, '2024-06-02', 80.20, 'Credit Card'),
(7, 7, '2024-07-14', 220.00, 'Debit Card'),
(8, 8, '2024-08-26', 130.10, 'PayPal'),
(9, 9, '2024-09-18', 500.00, 'Cash'),
(10, 10, '2024-10-23', 350.80, 'Credit Card');

```
### 3. **Invoices Table**
```sql
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    PaymentDate DATE,
    Amount DECIMAL(10, 2),
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert data
INSERT INTO Payments (PaymentID, OrderID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, 1, '2024-01-16', 100.50, 'Credit Card'),
(2, 2, '2024-02-11', 250.75, 'Debit Card'),
(3, 3, '2024-03-06', 150.30, 'PayPal'),
(4, 4, '2024-04-21', 300.00, 'Credit Card'),
(5, 5, '2024-05-11', 450.60, 'Cash'),
(6, 6, '2024-06-02', 80.20, 'Credit Card'),
(7, 7, '2024-07-14', 220.00, 'Debit Card'),
(8, 8, '2024-08-26', 130.10, 'PayPal'),
(9, 9, '2024-09-18', 500.00, 'Cash'),
(10, 10, '2024-10-23', 350.80, 'Credit Card');

```



## Title:  Group 4- G2-SCD-T234

## Group 4-  Reviews  , Discounts  , ShippingAddresses   

### 1. **Reviews  Table**
```sql
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY,
    ProductID INT,
    CustomerID INT,
    Rating INT,
    ReviewText TEXT,
    ReviewDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert data
INSERT INTO Reviews (ReviewID, ProductID, CustomerID, Rating, ReviewText, ReviewDate)
VALUES 
(1, 1, 1, 5, 'Excellent product!', '2024-01-15'),
(2, 2, 2, 4, 'Very good phone, but a bit expensive.', '2024-02-10'),
(3, 3, 3, 3, 'Good, but not what I expected.', '2024-03-05'),
(4, 4, 4, 5, 'Great sound quality!', '2024-04-20'),
(5, 5, 5, 4, 'Comfortable chair.', '2024-05-10'),
(6, 6, 6, 5, 'Love this tablet!', '2024-06-01'),
(7, 7, 7, 4, 'Works well, easy to use.', '2024-07-13'),
(8, 8, 8, 5, 'Perfect monitor!', '2024-08-25'),
(9, 9, 9, 4, 'Good mouse, affordable price.', '2024-09-17'),
(10, 10, 10, 5, 'Great keyboard for the price.', '2024-10-22');

```
### 2. **Discounts  Table**
```sql
CREATE TABLE Discounts (
    DiscountID INT PRIMARY KEY,
    ProductID INT,
    DiscountAmount DECIMAL(5, 2),
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Insert data
INSERT INTO Discounts (DiscountID, ProductID, DiscountAmount, StartDate, EndDate)
VALUES 
(1, 1, 100.00, '2024-01-01', '2024-01-31'),
(2, 2, 50.00, '2024-02-01', '2024-02-28'),
(3, 3, 10.00, '2024-03-01', '2024-03-31'),
(4, 4, 20.00, '2024-04-01', '2024-04-30'),
(5, 5, 30.00, '2024-05-01', '2024-05-31'),
(6, 6, 40.00, '2024-06-01', '2024-06-30'),
(7, 7, 15.00, '2024-07-01', '2024-07-31'),
(8, 8, 25.00, '2024-08-01', '2024-08-31'),
(9, 9, 5.00, '2024-09-01', '2024-09-30'),
(10, 10, 10.00, '2024-10-01', '2024-10-31');

```
### 3. **ShippingAddresses  Table**
```sql
CREATE TABLE ShippingAddresses (
    AddressID INT PRIMARY KEY,
    CustomerID INT,
    Address VARCHAR(200),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert data
INSERT INTO ShippingAddresses (AddressID, CustomerID, Address, City, State, ZipCode)
VALUES 
(1, 1, '123 Elm St', 'Somewhere', 'NY', '10001'),
(2, 2, '456 Oak St', 'Anywhere', 'CA', '20002'),
(3, 3, '789 Pine St', 'Anyplace', 'TX', '30003'),
(4, 4, '101 Maple St', 'Somewhere', 'FL', '40004'),
(5, 5, '202 Birch St', 'Elsewhere', 'IL', '50005'),
(6, 6, '303 Cedar St', 'Nowhere', 'OH', '60006'),
(7, 7, '404 Ash St', 'Everywhere', 'PA', '70007'),
(8, 8, '505 Redwood St', 'Someplace', 'WA', '80008'),
(9, 9, '606 Fir St', 'Anotherplace', 'AZ', '90009'),
(10, 10, '707 Pine St', 'Yetanotherplace', 'NC', '10010');

```
