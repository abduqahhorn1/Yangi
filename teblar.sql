CREATE TABLE Region (
    RegionID INT,
    RegionDescription VARCHAR(50)
);

CREATE TABLE Territories (
    TerritoryID VARCHAR(20),
    TerritoryDescription VARCHAR(50),
    RegionID INT
);

CREATE TABLE EmploveeTerritories (
    EmploveeID INT,
    TerritoryID VARCHAR(20)
);

CREATE TABLE Emplovees (
    EmploveeID INT,
    LastName VARCHAR(20),
    FirstName VARCHAR(10),
    Title VARCHAR(30) NOT NULL,
    TitleOfCountesy VARCHAR(25) NOT NULL,
    BirthDate DATETIME NOT NULL,
    HireDate DATETIME NOT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Region VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    Country VARCHAR(15) NOT NULL,
    HomePhone VARCHAR(24) NOT NULL,
    Extension VARCHAR(4) NOT NULL,
    Photo image NOT NULL,
    Notes text NOT NULL,
    ReportsTo INT NOT NULL,
    PhotoPath VARCHAR(255) NOT NULL
);

CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(40),
    SupplierID INT NOT NULL,
    CategoryID INT NOT NULL,
    QuantityPerUnit VARCHAR(20) NOT NULL,
    UnitPrice money,
    UnitslnStock smallint NOT NULL,
    UnitsOnOrder smallint NOT NULL,
    ReorderLevel smallint NOT NULL,
    Discontinued bit 
);


CREATE TABLE Order Details (
    OrderID INT,
    ProductID INT,
    UnitPrice money,
    Quantity smallint,
    Discount real
);

CREATE TABLE Orders (
    OrderID INT,
    CostomerID VARCHAR(5) NOT NULL,
    EmploveeID INT NOT NULL,
    OrderDate DATETIME NOT NULL,
    RequiredDate DATETIME NOT NULL,
    ShippedDate DATETIME NOT NULL,
    ShipVia INT NOT NULL,
    Freight money NOT NULL,
    ShipName  VARCHAR(40) NOT NULL,
    ShipAddress VARCHAR(60) NOT NULL,
    ShipCity VARCHAR(15) NOT NULL,
    ShipRegion VARCHAR(15) NOT NULL,
    ShipPostalCode VARCHAR(10) NOT NULL,
    ShipCountry VARCHAR(15) NOT NULL
);

CREATE TABLE Categories (
    CategoryID INT,
    CategoryName VARCHAR(15),
    Description text NOT NULL,
    Picture image NOT NULL
);

CREATE TABLE Suppliers (
    SupplierID INT,
    CompanyName VARCHAR(40),
    ContactName VARCHAR(30) NOT NULL,
    ContactTitle VARCHAR(30) NOT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Region VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    Country VARCHAR(15) NOT NULL,
    Phone VARCHAR(24) NOT NULL,
    Fax VARCHAR(24) NOT NULL,
    HomePage text NOT NULL
);

CREATE TABLE Customers (
    CustomerID VARCHAR(5),
    CompanyName VARCHAR(40),
    ContactName VARCHAR(30) NOT NULL,
    ContactTitle VARCHAR(30) NOT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Region VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    Country VARCHAR(15) NOT NULL,
    Phone VARCHAR(24) NOT NULL,
    Fax VARCHAR(24) NOT NULL
);

CREATE TABLE Shippers (
    ShipperID INT,
    CompanyName VARCHAR(40),
    Phone VARCHAR(24) NOT NULL
);