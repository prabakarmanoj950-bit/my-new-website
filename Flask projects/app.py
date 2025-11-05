from flask import Flask, jsonify, request,render_template,send_file,redirect,url_for
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
    return render_template('index.html')

# Registration page
@app.route('/register', methods=['GET'])
def get_registration():
    return   render_template('Registration_form.html')

# GET - Fetch all employees
@app.route('/submit', methods=['post'])
def user_details_adding():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone_number = request.form['contactno']
        course_type=request.form['dropbox']
        gender=request.form['gender']
        password=request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""INSERT INTO user_details (fname, lname, email, phone_number,password, gender, course_type)VALUES (%s,%s, %s, %s, %s, %s, %s)""", (fname, lname, email, phone_number,password, gender, course_type))
        conn.commit()
        conn.close()
        return render_template('Registration_form.html', message="Address added sucessfully")
    
    except Exception as e:
         return  jsonify({"error": str(e)}), 400 

@app.route('/home', methods=['post'])
def user_login_fn():
    #l_name=request.form['l_name']
    l_name=request.form.get('l_name', '')
    password=request.form['l_possword']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_details WHERE fname = %s AND password = %s", (l_name, password))
    get_values=cur.fetchall()
    conn.close()
    if len(get_values):
        return render_template('dashboard.html',user=get_values[0][1])
    else:
        return render_template('index.html',message="PLease put th correct password")

if __name__ == '__main__':
    app.run(debug=True)
