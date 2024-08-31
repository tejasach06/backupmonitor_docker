from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import date
import os

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Create a cursor object
    cursor = mysql.connection.cursor()

    # Get Start date and end date from user
    start_date = request.form.get('start_date', date.today().strftime("%Y-%m-%d"))
    end_date = request.form.get('end_date', date.today().strftime("%Y-%m-%d"))

    # Execute a SQL query to fetch data
    query = '''
    SELECT j.job_name, jr.start_time, jr.end_time, jr.status
    FROM jobs j LEFT JOIN job_runs jr ON j.job_id = jr.job_id
    WHERE DATE(jr.start_time) >= %s AND DATE(jr.start_time) <= %s
    '''
    cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()
    column_names = [c[0] for c in cursor.description]

    # Close the cursor
    cursor.close()

    # Pass the column names and rows to the template
    return render_template('index.html', column_names=column_names, rows=rows, start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


