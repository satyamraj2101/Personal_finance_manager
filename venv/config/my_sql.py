import mysql.connector
import sys
import os

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the settings.py file
settings_path = os.path.join(current_dir, 'settings.py')

# Add the directory path of the settings.py file to the Python path
sys.path.append(settings_path)

# Import the settings module
from settings import DATABASES



db_settings = DATABASES['default']

# Establish a connection
connection = mysql.connector.connect(
    user=db_settings['USER'],
    password=db_settings['PASSWORD'],
    host=db_settings['HOST'],
    database=db_settings['NAME']
)

# Check if the connection is successful
if connection.is_connected():
    print('Connected to the database!')

# Close the connection when done
connection.close()
