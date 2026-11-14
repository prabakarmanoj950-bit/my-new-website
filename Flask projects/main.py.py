from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Employee API is working"}

@app.get("/employees")
def get_employees():
    return [
        {"emp_id": 1, "emp_name": "Manoj"},
        {"emp_id": 2, "emp_name": "Rahul"}
    ]

