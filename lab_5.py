import psycopg2
import sqlite3
import random


def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name, email) VALUES (?, ?)", (name, email))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

def get_all():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    all_users = cursor.fetchall()
    return all_users

def get_one(id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    one_id = cursor.fetchone()
    return one_id

def delete_user_by_id(id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Создание таблицы "users"
#create_users_table()

# добавление нового пользователя
user_id = add_user("Андрей", "andruha228@mail.com")
print(f"Добавлен пользователь с id {user_id}")

all_users = get_all()
print("Все пользователи:")
for user in all_users:
    print(user)

user = get_one(user_id)
print(f"Пользователь с id {user_id}: {user}")
delete_user_by_id(6)

import sqlite3


def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()


def add_user(id, name, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", (id, name, email))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    conn.close()
    return all_users


def get_user_by_id(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def delete_user_by_id(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()


import random


def main():
    # create_users_table()

    id = random.randint(1, 1000)
    name = "Vasiliy Koshka"
    email = "vasyameow@mail.com"
    add_user(id, name, email)
    print(f"Добавлен пользователь {id, name, email}")

    print("Все пользователи:")
    all_users = get_all_users()
    for user in all_users:
        print(user)

    user_id = id
    get_one = get_user_by_id(user_id)
    print(f"Добавлен пользователь с id {user_id}: {name, email}")
    delete_user_by_id(user_id)
    print(f"Пользователь с id {user_id} удален")


if __name__ == "__main__":
    main()