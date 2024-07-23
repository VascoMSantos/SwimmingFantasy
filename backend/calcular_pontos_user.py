# cacular_pontos_user.py
# Purpose: Calculate the fantasey points of the user
# Autor: Vasco Santos
# Data de criação: 23/07/2024
# Direitos Autorais (c) 2024 Vasco Santos
# Todos os direitos reservados

from database.database_connection import create_connection, execute_query

def calculate_points(connection, user):
    query = "SELECT * FROM athletes WHERE club = %s"
    data = (user["club"],)
    execute_query(connection, query, data)

connection = create_connection("127.0.0.1", "root", "ytrewqMySQL99", "swimming_fantasy")

user = {}

calculate_points(connection, user)
print(f"User {user["club"]} points calculated successfully")