"""Versão corrigida do laboratório: usa consulta parametrizada sqlite3.

Compare com app.py para ver o que mudou e por quê.
"""

import sqlite3


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    )
    conn.execute("DELETE FROM users")
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ("admin", "1234"),
    )
    conn.commit()


def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    # SEGURO: placeholders (?) separam o comando dos dados.
    # O banco trata o input como valor, nunca como parte do SQL.
    cursor = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password),
    )
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
