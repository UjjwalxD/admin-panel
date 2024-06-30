from flask import Flask, render_template
print('http://127.0.0.1:6969/home')

app = Flask(__name__, static_folder='static', template_folder='templates')



@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=6969)
    