## Incremental Data Load Implementation for CO2 Emissions Dataset

## Overview
This document outlines the process for implementing incremental data loading for the vehicle CO2 emissions dataset into Azure MS SQL. The steps include utilizing a watermark table and applying data transformations such as aggregation and derived columns.

---

## Data Dictionary
### Dataset Columns
| Column Name                      | Data Type | Description                                                  |
| -------------------------------- | --------- | ------------------------------------------------------------ |
| Make                             | String    | Manufacturer or brand of the vehicle.                        |
| Model                            | String    | Specific model name or identifier of the vehicle.            |
| Vehicle Class                    | String    | Category or classification of the vehicle.                   |
| Engine Size (L)                  | Float     | Displacement volume of the vehicle's engine in liters.       |
| Cylinders                        | Integer   | Number of cylinders in the vehicle's engine.                 |
| Transmission                     | String    | Type of transmission system.                                 |
| Fuel Type                        | String    | Type of fuel used by the vehicle.                            |
| Fuel Consumption City (L/100 km) | Float     | Fuel consumption rate in liters per 100 km for city driving. |
| Fuel Consumption Hwy (L/100 km)  | Float     | Fuel consumption rate for highway driving.                   |
| Fuel Consumption Comb (L/100 km) | Float     | Fuel consumption rate for combined driving.                  |
| Fuel Consumption Comb (mpg)      | Float     | Fuel consumption rate in miles per gallon.                   |
| CO2 Emissions (g/km)             | Float     | Carbon dioxide emissions in grams per kilometer.             |

---




## Incremental Data Loading(IDL) using SQL Command

### Step 1: Source Identification

Step 1.1: Create the Main Table for CO2 Emissions Data
sql
```
CREATE TABLE CO2_Emissions (
    Make NVARCHAR(100),
    Model NVARCHAR(100),
    Vehicle_Class NVARCHAR(100),
    Engine_Size_L FLOAT,
    Cylinders INT,
    Transmission NVARCHAR(100),
    Fuel_Type NVARCHAR(50),
    Fuel_Consumption_City_L_100km FLOAT,
    Fuel_Consumption_Hwy_L_100km FLOAT,
    Fuel_Consumption_Comb_L_100km FLOAT,
    Fuel_Consumption_Comb_mpg FLOAT,
    CO2_Emissions_g_km FLOAT,
    Last_Updated DATETIME -- Column for tracking incremental updates
);
```

Step 1.2: Create the Watermark Table
sql 
```
CREATE TABLE Watermark (
    TableName NVARCHAR(100),
    LastUpdated DATETIME
);
```
Step 1.3: Insert Initial Data into the CO2_Emissions Table

```
INSERT INTO CO2_Emissions (
    Make, Model, Vehicle_Class, Engine_Size_L, Cylinders, Transmission,
    Fuel_Type, Fuel_Consumption_City_L_100km, Fuel_Consumption_Hwy_L_100km,
    Fuel_Consumption_Comb_L_100km, Fuel_Consumption_Comb_mpg,
    CO2_Emissions_g_km, Last_Updated
)
VALUES
('Toyota', 'Corolla', 'Compact', 1.8, 4, 'Automatic', 'Gasoline', 8.0, 6.5, 7.3, 32.0, 170.0, '2024-12-01 08:00:00'),
('Honda', 'Civic', 'Compact', 2.0, 4, 'Manual', 'Gasoline', 9.0, 7.0, 8.0, 29.0, 180.0, '2024-12-01 08:30:00'),
('Ford', 'F-150', 'Truck', 3.5, 6, 'Automatic', 'Diesel', 15.0, 12.0, 13.5, 20.0, 350.0, '2024-12-01 09:00:00');
```

Step 1.4: Insert the Initial Watermark Record
```
INSERT INTO Watermark (TableName, LastUpdated)
VALUES ('CO2_Emissions', '2024-12-01 09:00:00');
```

Step 1.5: Query for Incremental Data Load Based on Watermark
```
DECLARE @LastUpdated DATETIME;
SELECT @LastUpdated = LastUpdated
FROM Watermark
WHERE TableName = 'CO2_Emissions';
```

-- Fetch new or updated records from the source (pseudo-code for demonstration)
-- Replace with an actual query from your source system

```
SELECT *
FROM Source_CO2_Emissions
WHERE Last_Updated > @LastUpdated;
```
Step 1.6: Update Watermark After Loading New Records
-- Assuming the new data is already inserted into CO2_Emissions

```
UPDATE Watermark
SET LastUpdated = (SELECT MAX(Last_Updated) FROM CO2_Emissions)
WHERE TableName = 'CO2_Emissions';
```

## Step 2: Incremental Data Load(IDL) using Azure Data Factory(ADF)

This step involves the process of taking the newly extracted data (based on the `Last_Updated` timestamp from the `Watermark` table) and loading it into the `CO2_Emissions` table, ensuring that:

- New records are inserted.
- Updated records are correctly updated.
- The watermark is refreshed after a successful load.

### Step 2.1: Extract Data from the Source

You’ve already outlined the process to get the last updated timestamp from the `Watermark` table, and you’ve written pseudo-code to pull data based on the `Last_Updated` field:

``` sql
DECLARE @LastUpdated DATETIME;

-- Get the last update timestamp from the Watermark table
SELECT @LastUpdated = LastUpdated
FROM Watermark
WHERE TableName = 'CO2_Emissions';

-- Extract records that have been updated after the last watermark timestamp
SELECT *
FROM Source_CO2_Emissions
WHERE Last_Updated > @LastUpdated;
```



### Step 3: Incremental Data Extraction
Query the source dataset to extract records with a last_updated timestamp greater than the value in the Watermark table.

---





## Transformations

### Aggregations
1. Aggregations summarize data based on specific columns to generate insights.
   - Average CO2 Emissions by Vehicle Class:

```
sql
SELECT 
    Vehicle_Class,
    AVG(CO2_Emissions_g_km) AS Avg_CO2_Emissions
FROM CO2_Emissions
GROUP BY Vehicle_Class;
```

-- Maximum Fuel Efficiency by Make:

```  
sql
SELECT 
    Make,
    MAX(Fuel_Consumption_Comb_mpg) AS Max_Fuel_Efficiency
FROM CO2_Emissions
GROUP BY Make;
```

### Derived Columns
1. Derived columns create new values based on existing ones.

-- Emissions Range Categorization:

```  
sql
SELECT 
    *,
    CASE 
        WHEN CO2_Emissions_g_km < 100 THEN 'Low'
        WHEN CO2_Emissions_g_km BETWEEN 100 AND 200 THEN 'Medium'
        ELSE 'High'
    END AS Emissions_Range
FROM CO2_Emissions;
```

-- Efficiency Rating:

```
sql
SELECT 
    *,
    CASE 
        WHEN Fuel_Consumption_Comb_mpg > 30 THEN 'Efficient'
        WHEN Fuel_Consumption_Comb_mpg BETWEEN 20 AND 30 THEN 'Moderate'
        ELSE 'Inefficient'
    END AS Efficiency_Rating
FROM CO2_Emissions;
```


## Next Steps
# ETL Pipeline Implementation for Vehicle CO2 Emissions Dataset using Azure Data Factory

This document provides a step-by-step guide to implement an ETL (Extract, Transform, Load) pipeline for the **Vehicle CO2 Emissions dataset** using **Azure Data Factory (ADF)**. The pipeline will extract data from a source system, transform it according to business logic, and load it into an Azure SQL Database.

---

## **Step 1: Develop the ETL Pipeline**

### **1.1. Extract Phase**

In this phase, we will pull the data from the source system and filter the data based on the `Last_Updated` column to perform incremental loads.

#### **1.1.1. Create Linked Service for the Source System**
1. Create a **Linked Service** in ADF to connect to the source system (e.g., Azure Blob Storage, SQL Server, REST API).
2. Configure authentication and connection details as required.

#### **1.1.2. Create Dataset for the Source Data**
1. Define a **Dataset** in ADF that points to the source system. This could be a file (e.g., CSV, Parquet) or a database table.
2. Specify the data format and metadata, such as the file location or table schema.

#### **1.1.3. Incremental Data Load using `Last_Updated`**
1. Implement a **filtering mechanism** to load only the data that has been updated since the last extraction using the `Last_Updated` column.
2. Store the timestamp of the last data load in a **watermark table** or **Azure Table Storage** to keep track of the last loaded data.
3. The query to extract the data could look like this (SQL example):

   ```sql
   SELECT * 
   FROM Vehicle_CO2_Emissions
   WHERE Last_Updated > @Last_Loaded_Timestamp
