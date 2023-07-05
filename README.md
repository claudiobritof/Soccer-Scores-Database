# Soccer-Scores-Database
Retrieves soccer game results from a specified API endpoint and stores them in a MySQL database.  
  
&emsp;This Python script retrieves soccer game results from an API and stores them in a MySQL database. It uses the requests library to make API requests and the mysql.connector module to establish a connection with the MySQL database.  

In the API you will find results of matches of different sports.  
API URL: https://rapidapi.com/theoddsapi/api/live-sports-odds/  

<b>Prerequisites:  </b>  
  
To run this script, you need to have Python installed on your system. The code is compatible with Python 3. Additionally, ensure that you have the following dependencies installed:  
  
&emsp;•	requests  
&emsp;•	mysql-connector-python  

<b>Setup:  </b>  
1.	Clone the project repository or copy the code into a Python file.  
2.	Install the necessary dependencies by running the following command:  
Copy code  
pip install requests mysql-connector-python   
3.	Make sure you have a MySQL database set up and running.  
4.  Obtain an API key by signing up at RapidAPI. Once you have the API key, replace the value of the X-RapidAPI-Key header in the following line:
  
&emsp;headers = { "X-RapidAPI-Key": "YOUR_API_KEY" }  
&emsp;Replace "YOUR_API_KEY" with your own API key.  
&ensp;5.	Update the script with your own database connection details. On the "config.json" file, located on .gitignore, I wrote this structure (in a .json):  
  
{  
  "api_key": "YOUR_API_KEY",  
  "db_host": "YOUR_DB_HOST",  
  "db_user": "YOUR_DB_USER",  
  "db_password": "YOUR_DB_PASSWORD",  
  "db_name": "YOUR_DB_NAME",  
  "db_auth_plugin": "YOUR_AUTH_PLUGIN"  
}  
  
Replace the values in the host, user, password, database name and authentication plugin parameters with your own MySQL database credentials.  
6.	Run the Python script using your preferred method (e.g., command line, IDE, etc.).  

<b>Usage:  </b>  
  
This script retrieves soccer game results from the specified API endpoint and stores them in a MySQL database table called matches_brasileirao_serie_a_2023. The table has the following columns: