from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Database connection parameters
server = 'APL69954'
database = 'hardware'
username = 'apposcr'
password = '2#06A9a'
driver = '{SQL Server}'

# Route to display the webpage
@app.route('/')
def index():
    return render_template('new.html')

# Route to handle form submission
# PROGRAMMER : APL69954
@app.route('/search', methods=['POST'])
def search():
    shop_id = request.form.get('shop_id')

    try:
        with pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}') as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM [ADDRESS_DATA] WHERE shop_id=?", (shop_id,))
                result = cursor.fetchone()
    except Exception as e:
        # Handle the exception, log it, or return an error message to the user
        return render_template('error.html', error_message=str(e))

    return render_template('new.html', result=result)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
