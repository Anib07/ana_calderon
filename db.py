import sqlite3
from datetime import datetime

DB_FILE = "ani_trivia.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    return conn

# --- Guardar puntaje ---
def save_score(user_id, score, category, difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO scores (user_id, score, category, difficulty, date_played)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, score, category, difficulty, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# --- Obtener preguntas ---
def get_questions(category, difficulty):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM questions WHERE category=? AND difficulty=?
    """, (category, difficulty))
    result = cursor.fetchall()
    conn.close()
    return result

# --- Registrar usuario ---
def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


# --- Verificar usuario (login) ---
def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return user  # devuelve diccionario con id, username, password
    else:
        return None

