# insert_athletes.py
# Purpose: Insert athletes into the database
# Autor: Vasco Santos
# Data de criação: 17/07/2024
# Direitos Autorais (c) 2024 Vasco Santos
# Todos os direitos reservados

import mysql.connector
from mysql.connector import Error
from database_connection import create_connection, execute_query

def insert_athlete(connection, athlete):
    query = "INSERT INTO athletes (first_name, last_name, age, gender, club) VALUES (%s, %s, %s, %s, %s)"
    data = (athlete["first_name"], athlete["last_name"], athlete["age"], athlete["gender"], athlete["club"])
    execute_query(connection, query, data)

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

insert_athlete(connection, athlete1)
print(f"Athlete {athlete1["first_name"]} {athlete1["last_name"]} inserted successfully")
insert_athlete(connection, athlete2)
print(f"Athlete {athlete2["first_name"]} {athlete2["last_name"]} inserted successfully")
insert_athlete(connection, athlete3)
print(f"Athlete {athlete3["first_name"]} {athlete3["last_name"]} inserted successfully")