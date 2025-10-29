import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",  # tu contraseña
    "database": "ani_trivia"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def check_user(username, password):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    return None

def register_user(username, password):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()


def save_score(user_id, score, category, difficulty):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO scores (user_id, score, category, difficulty) VALUES (%s, %s, %s, %s)",
                (user_id, score, category, difficulty)
            )
            conn.commit()
        except Exception as e:
            print("Error al guardar score:", e)
        finally:
            cursor.close()
            conn.close()

