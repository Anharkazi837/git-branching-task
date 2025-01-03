# Databricks notebook source
!pip install yfinance

# COMMAND ----------

#Install the ODBC Driver 18 for SQL Server


%pip install pyodbc

# Add the Microsoft package repository and install the ODBC driver
!curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
!curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
!apt-get update
!ACCEPT_EULA=Y apt-get install -y msodbcsql18

%restart_python

# COMMAND ----------

from pyspark.dbutils import DBUtils
dbutils = DBUtils(spark)

# COMMAND ----------

dbutils.widgets.text("StockName", "")
StockName = dbutils.widgets.get("StockName")

# COMMAND ----------

import yfinance as yf
import pandas as pd
stock = yf.Ticker(StockName)
stock_df = pd.DataFrame(stock.info)

# COMMAND ----------

columns_list = stock_df.columns.tolist()
columns_list


# COMMAND ----------

from datetime import datetime
columns_list = stock_df.columns.tolist()
stock_details = stock_df[columns_list].head(1)
# Add current time as a new column in string format
stock_details['record_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
stock_details_ordered= [
    'record_time',
    'shortName',
    'currentPrice',
    'previousClose',
    'open',
    'dayLow',
    'dayHigh',
    'fiftyTwoWeekLow',
    'fiftyTwoWeekHigh',
    'volume',
    'marketCap',
    'currency',
    ]
stock_details = stock_details[stock_details_ordered]

# Rename the column 'open' to 'today_open'
stock_details.rename(columns={'open': 'today_open'}, inplace=True)
stock_details.rename(columns={'shortName': 'short_name'}, inplace=True)



# COMMAND ----------

display(stock_details)

# COMMAND ----------

table_name = "stock_details_" + stock_details['short_name'].iloc[0].split()[0]

# COMMAND ----------

# Define the JDBC connection properties
jdbc_hostname = "server4everyone.database.windows.net"
jdbc_port = 1433  # Default port for SQL Server
jdbc_database = "db4everyone"
jdbc_username = "adminuser@server4everyone"
jdbc_password = "Localhost@1234567"

# JDBC URL
jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};database={jdbc_database}"

# Connection properties
connection_properties = {
    "user": "adminuser",
    "password": "Localhost@1234567",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# COMMAND ----------

# Convert pandas DataFrame to PySpark DataFrame
stock_details = spark.createDataFrame(stock_details)

# COMMAND ----------

# Write the DataFrame to the Azure SQL Database
# stock_details.write.jdbc(
#     url=jdbc_url,
#     table="sujay_StockDetails",
#     mode="append",  # Use "append" if you want to add to an existing table
#     properties=connection_properties
# )

# COMMAND ----------

# Define the JDBC connection properties
jdbc_hostname = "server4everyone.database.windows.net"
jdbc_port = 1433  # Default port for SQL Server
jdbc_database = "db4everyone"
jdbc_username = "adminuser@server4everyone"
jdbc_password = "Localhost@1234567"

# Define the function to write DataFrame to SQL Server
def write_to_sql(stock_details, table_name):
    # JDBC connection properties
    jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};database={jdbc_database}"
    connection_properties = {
        "user": "adminuser",
        "password": "Localhost@1234567",
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }
    # Call the stored procedure to create the table if it doesn't exist
    import pyodbc
    # Define the connection parameters
    conn_str =(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=tcp:server4everyone.database.windows.net;DATABASE=db4everyone;UID=adminuser;PWD=Localhost@1234567'
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("EXEC CreateTableIfNotExists_Sujay ?", table_name)
    conn.commit()
    conn.close()
    
    # Write DataFrame to SQL Server
    stock_details.write.jdbc(url=jdbc_url, table=table_name, mode="append", properties=connection_properties)

# Example usage
write_to_sql(stock_details, table_name)

