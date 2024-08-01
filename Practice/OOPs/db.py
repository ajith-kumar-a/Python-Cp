import psycopg2
from psycopg2 import sql

def connect_to_postgresql():
    try:
        # Connect to your postgres DB
        connection = psycopg2.connect(
            host="localhost",       # e.g., "localhost" or "127.0.0.1"
            user="postgres",       # e.g., "postgres"
            password="Database@123",  # e.g., "password"
            database="exercises"  # e.g., "mydatabase"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT version();")

        # Fetch the result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        # Example: Create a table
        create_table_query = '''
        CREATE TABLE example_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
        '''
        # cursor.execute(create_table_query)
        # connection.commit()
        # print("Table created successfully")

        # Example: Insert data
        insert_data_query = '''
        INSERT INTO example_table (name, age) VALUES (%s, %s);
        '''

        name = input("Enter Name: ")
        age = int(input("Enter Age : "))

        cursor.execute(insert_data_query, (name, age))
        connection.commit()
        print("Data inserted successfully")

        # Example: Retrieve data
        cursor.execute("SELECT * FROM example_table;")
        records = cursor.fetchall()
        print("Retrieved data:")
        for row in records:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

connect_to_postgresql()
