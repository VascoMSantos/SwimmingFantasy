# delete_athletes.py
# Purpose: Insert athletes into the database
# Autor: Vasco Santos
# Data de criação: 17/07/2024
# Direitos Autorais (c) 2024 Vasco Santos
# Todos os direitos reservados

from database.database_connection import create_connection, execute_query

def delete_athlete(connection, athlete):
    query = "DELETE FROM athletes WHERE first_name = %s AND last_name = %s"
    data = (athlete["first_name"], athlete["last_name"])
    execute_query(connection, query, data)

def reset_table(connection):
    query = "TRUNCATE TABLE athletes"
    execute_query(connection, query, None)

connection = create_connection("127.0.0.1", "root", "ytrewqMySQL99", "swimming_fantasy")

athlete1 = {
    "first_name": "Tamila",
    "last_name": "Holub",
    "age": 25,
    "gender": "Female",
    "club": "Sporting Clube de Braga",
    }

athlete2 = {
    "first_name": "Miguel",
    "last_name": "Nascimento",
    "age": 27,
    "gender": "Male",
    "club": "Sport Lisboa e Benfica",
    }

athlete3 = {
    "first_name": "Diogo",
    "last_name": "Ribeiro",
    "age": 20,
    "gender": "Male",
    "club": "Sport Lisboa e Benfica",
    }

status = "delete_all_athletes"
print(f"Status: {status}")
if status == "delete_athletes":
    delete_athlete(connection, athlete1)
    print(f"Athlete {athlete1["first_name"]} {athlete1["last_name"]} deleted successfully")
    delete_athlete(connection, athlete2)
    print(f"Athlete {athlete2["first_name"]} {athlete2["last_name"]} deleted successfully")
    delete_athlete(connection, athlete3)
    print(f"Athlete {athlete3["first_name"]} {athlete3["last_name"]} deleted successfully")
elif status == "delete_all_athletes":
    reset_table(connection)
    print("All athletes deleted successfully")