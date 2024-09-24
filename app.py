from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alphabet')
def alphabet():
    return render_template('alphabet.html')


@app.route('/words')
def words():
    return render_template('words.html')

if __name__=='__main__':
    app.run(debug=True)