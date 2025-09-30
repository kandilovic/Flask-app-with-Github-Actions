from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Get ENV variables (passed from Docker Compose)
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Hello, Flask + Postgres! 🚀<br>Connected to: {db_version}"
    except Exception as e:
        return f"Error connecting to DB: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
