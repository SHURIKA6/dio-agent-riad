# LABORATÓRIO - NÃO USAR EM PROD
"""Exemplo vulnerável de laboratório para estudar SQL injection.

Execute apenas na sua máquina, com dados fictícios.
O objetivo é o DIO Agent te ajudar a achar a falha e corrigir.
"""

import sqlite3


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    )
    conn.execute("DELETE FROM users")
    conn.execute(
        "INSERT INTO users (username, password) VALUES ('admin', '1234')"
    )
    conn.commit()


def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    # VULNERÁVEL de propósito: concatena o input direto na query.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = conn.execute(query)
    return cursor.fetchone() is not None


if __name__ == "__main__":
    db = sqlite3.connect(":memory:")
    init_db(db)

    user = input("Usuário: ")
    pwd = input("Senha: ")

    if login(db, user, pwd):
        print("Login OK!")
    else:
        print("Login falhou.")
