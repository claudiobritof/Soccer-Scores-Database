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
  
&emsp;&emsp;&emsp;headers = { "X-RapidAPI-Key": "YOUR_API_KEY" }  
&emsp;&emsp;&emsp;Replace "YOUR_API_KEY" with your own API key.  
&emsp;5.	Update the script with your own database connection details.  
&emsp;&emsp;On the "config.json" file, located on .gitignore, I wrote this structure (in a .json):  
  
&emsp;&emsp;{  
&emsp;&emsp;  "api_key": "YOUR_API_KEY",  
&emsp;&emsp;  "db_host": "YOUR_DB_HOST",  
&emsp;&emsp;  "db_user": "YOUR_DB_USER",  
&emsp;&emsp;  "db_password": "YOUR_DB_PASSWORD",  
&emsp;&emsp;  "db_name": "YOUR_DB_NAME",  
&emsp;&emsp;  "db_auth_plugin": "YOUR_AUTH_PLUGIN"  
&emsp;&emsp;}  
  
&emsp;Replace the values in the API key, host, user, password, database name and authentication plugin parameters with your own MySQL  
&emsp;database credentials.  
&emsp;6.	Run the Python script using your preferred method (e.g., command line, IDE, etc.).  

<b>Usage:  </b>  
  
This script retrieves soccer game results (year: 2023) from the specified API endpoint and stores them in a MySQL database table called matches_brasileirao_serie_a_2023. The table has the following columns:  
  
&emsp;•	datahora_partida: The date and time of the game;  
&emsp;•	data_partida: The date of the game;  
&emsp;•	time_casa: The home team name;  
&emsp;•	time_fora: The away team name;  
&emsp;•	gols_time_casa: The number of goals scored by the home team;  
&emsp;•	gols_time_fora: The number of goals scored by the away team;  

The script performs the following steps:
1.	Makes a request to the API endpoint specified by url_odds and retrieves the game results.
2.	Establishes a connection with the MySQL database using the provided credentials.
3.	Creates a table named matches_brasileirao_serie_a_2023 if it doesn't exist already.
4.	Extracts the desired information from the game scores and stores them in the matches list.
5.	Inserts the data from the matches list into the MySQL database table using the executemany method.
6.	Commits the changes to the database and closes the database connection.
Make sure you have the necessary permissions and privileges to create tables and insert data into the specified database.
  
Contributions are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
  
MIT License
