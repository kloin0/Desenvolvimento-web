from flask import Flask, render_template

app = Flask(__name__)
@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')
@app.route('/conversor')
def conversor():
    return render_template('conversor.html')
if __name__ == '__main__':
    app.run(debug=True)
    