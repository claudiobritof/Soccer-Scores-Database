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
4.	Update the script with your own database connection details. Modify the following lines:  







pythonCopy code  
db_connection = mysql.connector.connect( host="localhost", user="claudio_git", password="public4At&H4r7pass", database="h2_testdb" ) 
Replace the values in the host, user, password, and database parameters with your own MySQL database credentials.
5.	Obtain an API key by signing up at RapidAPI. Once you have the API key, replace the value of the X-RapidAPI-Key header in the following line:
pythonCopy code
headers = { "X-RapidAPI-Key": "d20f30e63dmsh95f7a23c5519e24p15eca4jsn4573a4bff139" } 
Replace "d20f30e63dmsh95f7a23c5519e24p15eca4jsn4573a4bff139" with your own API key.  
6.	Run the Python script using your preferred method (e.g., command line, IDE, etc.).  

<b>Usage:  </b>  
  
This script retrieves soccer game results from the specified API endpoint and stores them in a MySQL database table called matches_brasileirao_serie_a_2023. The table has the following columns: