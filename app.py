from flask import Flask, render_template
from database.connector import connect 
print('http://127.0.0.1:6969/home')
connect.database()




app = Flask(__name__, static_folder='static', template_folder='templates')



@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=6969)
    