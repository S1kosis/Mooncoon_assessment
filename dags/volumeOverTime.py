from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import duckdb

# Define your DAG
dag = DAG('volumeOverTime', start_date=datetime(2023, 9, 20), schedule_interval=None)

# Define a Python function to execute the SQL query and display the results
def execute_and_display_query():
    # Connect to the DuckDB database
    con = duckdb.connect(database='./data/ethereum.snappy.parquet')
    
    # Define the SQL query you want to execute
    sql_query = """
    SELECT SUM(transaction_count) AS Total_Transactions,
        SUM(size) AS Total_Eth,
        HOUR(timestamp) AS The_Hour
        FROM 'ethereum.snappy.parquet'
        GROUP BY The_Hour
        ;
    """
    
    # Execute the SQL query and fetch the results
    result = con.execute(sql_query)
    
    # Fetch all rows from the result set
    rows = result.fetchall()
    
    # Display the results
    for row in rows:
        print(f"Date: {row[0]}, Transaction Count: {row[1]}, Total Value: {row[2]} ETH")

# Define a PythonOperator to run the function
query_task = PythonOperator(
    task_id='execute_and_display_query',
    python_callable=execute_and_display_query,
    dag=dag
)