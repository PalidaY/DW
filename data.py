import pandas as pd
import config
import mysql.connector

db_config = config.db_params

df = pd.read_csv("data/shipping.csv")

# Test database
with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        # Execute a simple query to test the connection
        cursor.execute("SELECT 1")
        # Optionally, fetch the result to verify (not strictly necessary for a connection test)
        test_result = cursor.fetchone()
        print("Connection test successful:", test_result)

# Insert
with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        # Prepare your INSERT statement
        insert_query = """
        INSERT INTO delivery_company_db 
        (company_name, services, phone_number, email, address, state, country)
        VALUES 
        (%s, %s, %s, %s, %s, %s, %s);
        """
        
        # Convert the DataFrame to a list of tuples
        data_tuples = list(df.itertuples(index=False, name=None))
        
        # Execute the bulk insert
        cursor.executemany(insert_query, data_tuples)
        
        # The connection is not closed here, but the cursor is properly managed
        # The connection will be closed when exiting the outer `with` block

    # Commit the transaction outside of the cursor's `with` block
    conn.commit()
