
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('playground1.html')

@app.route('/play/<num>')
def play2(num):
    return render_template('playground2.html', some_num = int(num))

@app.route('/play/<num>/<color>')
def play3(num, color):
    return render_template('playground3.html', some_num = int(num), some_color = color)









if __name__ == '__main__':
    app.run(debug=True)