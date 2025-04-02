# import mysql.connector
# from mysql.connector import Error

# db_name = "library2025"
# user = 'root'
# password = 'Lynn060386!'
# host = 'localhost'

# try:
#     conn = mysql.connector.connect(
#         database = db_name,
#         user = user,
#         password = password,
#         host = host
#     )

#     if conn.is_connected():
#         print("Connected to MySQL database successfully")
# except Error as e:
#     print(f"Error: {e}")
# finally:
#     if conn and conn.is_connected():
#         conn.close()
#         print("MySQL connection is closed.")




import mysql.connector
from mysql.connector import Error

def connect_database():
    '''Connect to the MySQL database and return the connection object'''
    # Database connection parameters
    db_name = 'library2025'
    user = 'root'
    password = 'Lynn060386!'
    host = 'localhost'

    try:
        # Attempting to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None
