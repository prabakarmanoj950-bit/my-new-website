from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        os.environ["postgresql://postgres:[Qwerty@12345]@db.brpghinhqpoyvzutuhzz.supabase.co:5432/postgres"]
    )


@app.get("/")
def home():
    return {"message": "Employee API is working"}

'''@app.get("/employees")
def get_employees():
    return [
        {"emp_id": 1, "emp_name": "Manoj"},
        {"emp_id": 2, "emp_name": "Rahul"}
    ]'''

@app.get("/employees")
def get_employees():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT emp_id, emp_name
        FROM employees
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"emp_id": row[0], "emp_name": row[1]}
        for row in rows
    ]
