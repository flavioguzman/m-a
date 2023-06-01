import psycopg2
import pandas as pd

def extract_data(limit=100):
    """
    Extracts data from PostgreSQL and writes it to a JSON file.

    Parameters:
    limit (int): Number of rows to limit for testing.

    Returns:
    None
    """
    try:
        # Connect to your postgres DB
        connection = psycopg2.connect(
            dbname="medicalacademy",
            user="flavio",
            password="12345",
            host="localhost"  # adjust if your DB isn't hosted locally
        )

        # Open a cursor to perform database operations
        cur = connection.cursor()

        # Query the database, limit rows for testing
        query = f"SELECT * FROM indications_stitch LIMIT {limit}"
        data_frame = pd.read_sql_query(query, connection)

        # Close DB connection
        cur.close()
        connection.close()

        # Save dataframe to JSON
        data_frame.to_json("data.json", orient="records")

        print(f"Data extracted successfully, check data.json file.")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)


if __name__ == "__main__":
    extract_data(50)  # adjust limit as needed for testing
