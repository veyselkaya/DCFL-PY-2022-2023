from flask import Flask, render_template, request, redirect, url_for, flash
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/toplama', methods=['GET', 'POST'])
def toplama():
    if request.method == 'POST':
        sayi1 = request.form['sayi1']
        sayi2 = request.form['sayi2']
        sonuc = float(sayi1) + float(sayi2)

        return render_template('toplama.html', sonuc = sonuc)
    return render_template('toplama.html')


@app.route('/usalma', methods= ['GET', 'POST'])
def usalma():
    if request.method == "POST":
        sayi1 = request.form['sayi1']
        sayi2 = request.form['sayi2']
        sonuc = pow(int(sayi1), int(sayi2))

        return render_template('usalma.html', sonuc= sonuc)
    return render_template('usalma.html')



if __name__ == '__main__':
    app.run(debug=True)