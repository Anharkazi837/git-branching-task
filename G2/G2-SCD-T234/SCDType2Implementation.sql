---- CREATE HISTORY TABLE ---------------

CREATE TABLE Employees_priya (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
	StartDate DATETIME, 
	EndDate DATETIME, 
	IsCurrent BIT
);
--drop table Employees_priya
--- INSERT DATA INTO EMPLOYEES--------

INSERT INTO Employees_priya (EmployeeID, FirstName, LastName, Department, Salary,StartDate,EndDate,IsCurrent)
VALUES 
(1, 'John', 'Adams', 'Sales', 55000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(2, 'Emma', 'Clark', 'Marketing', 65000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(3, 'Olivia', 'Taylor', 'HR', 60000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(4, 'James', 'Davis', 'Engineering', 70000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(5, 'Ava', 'Miller', 'Operations', 75000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(6, 'Noah', 'Brown', 'IT', 80000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(7, 'Liam', 'Wilson', 'Finance', 90000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(8, 'Sophia', 'Moore', 'Sales', 45000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(9, 'Lucas', 'Martin', 'Marketing', 48000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1),
(10, 'Mia', 'Lee', 'HR', 42000.00,'2022-04-22 10:34:23','9999-01-01 10:34:23',1);

----- CRAETE INCOMING TABLE -----------------
CREATE TABLE INCOMING_Employees_priya (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2))

	----------- INSERT DATA INTO INCOMING TABLE ---------
	INSERT INTO INCOMING_Employees_priya (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(1, 'John', 'Adams', 'Marketing', 75000.00),
(2, 'Emma', 'Clark', 'Marketing', 85000.00),
(3, 'Olivia', 'Taylor', 'HRHead', 90000.00),
(4, 'James', 'Davis', 'Engineering', 90000.00)

------- Creating sp for scd2 --------------
ALTER PROCEDURE dbo.usp_SCD2_ImplementationPriya
as 
begin 
-- Update existing records
UPDATE Employees_priya
SET EndDate = GETDATE(),IsCurrent=0
WHERE EmployeeID IN (
    SELECT EmployeeID FROM INCOMING_Employees_priya
 --   EXCEPT
  --  SELECT EmployeeID FROM Employees_priya WHERE IsCurrent = 1
) AND IsCurrent=1;

INSERT INTO Employees_priya (EmployeeID, FirstName, LastName, Department, Salary,StartDate,EndDate,IsCurrent)
SELECT EmployeeID, FirstName, LastName, Department, Salary, GETDATE(), '9999-01-01 10:34:23', 1
FROM INCOMING_Employees_priya
WHERE EXISTS (
    SELECT 1 FROM Employees_priya WHERE Employees_priya.EmployeeID = INCOMING_Employees_priya.EmployeeID
);
 

end

exec dbo.usp_SCD2_ImplementationPriya
select * from Employees_priya
select * from INCOMING_Employees_priya
