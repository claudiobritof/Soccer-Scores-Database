import requests
import mysql.connector
import json
from datetime import datetime

# Describing a request do receive, using the API, the games results:
url_odds = "https://odds.p.rapidapi.com/v4/sports/soccer_brazil_campeonato/scores"

# Reading the configuration file (which is located on .gitignore):
with open("config.json") as c:
    config = json.load(c)

# Retrieve the values:
api_key = config["api_key"]
db_host = config["db_host"]
db_user = config["db_user"]
db_password = config["db_password"]
db_name = config["db_name"]
db_auth_plugin = config["auth_plugin"]

headers = {
    "X-RapidAPI-Key": api_key
}
params = {
    "region": "br",
    "season": "2023"
}

# Requesting API:
response = requests.get(url_odds, headers=headers, params=params)

# Storaging the request return in a variable:
requested_data = response.json()
print(response.headers)
print(response.content)

# Connection with MySQL database:
db_connection = mysql.connector.connect(
    host= db_host,
    user= db_user,
    password= db_password,
    database= db_name,
    auth_plugin= db_auth_plugin
)

db_cursor = db_connection.cursor(buffered=True)

# Creating table:
create_table_query = """
CREATE TABLE IF NOT EXISTS matches_brasileirao_serie_a_2023 (
    datahora_partida DATETIME,
    data_partida DATE,
    time_casa VARCHAR(255),
    time_fora VARCHAR(255),
    gols_time_casa INT,
    gols_time_fora INT
)
"""
db_cursor.execute(create_table_query)

# Inserting data on table:
insert_query = """
INSERT INTO matches_brasileirao_serie_a_2023
(datahora_partida, data_partida, time_casa, time_fora, gols_time_casa, gols_time_fora)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Extracting information I wanna use from games scores:
matches = []
for match in requested_data:
    datahora_partida_str = match["commence_time"]
    datahora_partida = datetime.strptime(
        datahora_partida_str, '%Y-%m-%dT%H:%M:%SZ')
    data_partida = datahora_partida.date()
    time_casa = match["home_team"]
    time_fora = match["away_team"]
    score = match.get("score")
    gols_time_casa = match.get("home_team_score", None)
    gols_time_fora = match.get("away_team_score", None)
    event = (datahora_partida, data_partida, time_casa,
               time_fora, gols_time_casa, gols_time_fora)
    matches.append(event)

db_cursor.execute("SELECT * FROM matches_brasileirao_serie_a_2023")
column_names = [column[0] for column in db_cursor.description]

print(column_names)
print(requested_data)
print(datahora_partida) #match_datetime
print(data_partida) #match_date
print(time_casa) #home_team
print(time_fora) #away_team
print(gols_time_casa) #home_team_goals
print(gols_time_fora) #away_team_goals
print(event)
print(matches)

db_cursor.executemany(insert_query, matches)

# Committing changes and closing connection with database:
db_connection.commit()
db_cursor.close()
db_connection.close()