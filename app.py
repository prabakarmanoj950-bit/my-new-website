from flask import Flask, jsonify, request,render_template,send_file
import psycopg2



app = Flask(__name__)

# Sample data
employees = [
    {"id": 1, "name": "Manoj", "role": "Developer"},
    {"id": 2, "name": "Prabakar", "role": "Analyst"}
]



# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Qwerty@12345",
        host="localhost",
        port="5432"
    )
    return conn


# Home route
@app.route('/')
def home():
    website_name = request.host
    return website_name
   # return send_file('index.html')

# Registration page
@app.route('/register', methods=['GET'])
def get_registration():
    return   send_file('Registration_form.html')

# GET - Fetch all employees
@app.route('/submit', methods=['post'])
def user_details_adding():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phone_number = request.form['contactno']
    course_type=request.form['dropbox']
    gender=request.form['gender']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO user_details (fname, lname, email, phone_number, gender, course_type)VALUES (%s, %s, %s, %s, %s, %s)""", (fname, lname, email, phone_number, gender, course_type))
    conn.commit()
    conn.close()
    return send_file('Registration_form.html', message="Address added sucessfully")

if __name__ == '__main__':
    app.run(debug=True)
