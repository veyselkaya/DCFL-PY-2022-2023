from flask import Flask, render_template, request, url_for, redirect
import math


app = Flask(__name__)



@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']


        if request.form.get('add'):
            sonuc = int(num1) + int(num2)
            islem = "Toplama işlemi"
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2, islem=islem)
        elif request.form.get('subtrack'):
            sonuc= int(num1) - int(num2)
            islem = "Çıkarma işlemi"
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2, islem=islem)
        elif request.form.get('multply'):
            sonuc= int(num1) * int(num2)
            islem = "Çarpma işlemi"
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2, islem=islem)
        elif request.form.get('divide'):
            sonuc= int(num1) / int(num2)
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2)
        elif request.form.get('power'):
            sonuc= int(num1) ** int(num2)
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2)
        elif request.form.get('root'):
            sonuc= int(num1) ** (1/int(num2))
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2)
        elif request.form.get('mod'):
            sonuc = int(num1) % int(num2)
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2)
        elif request.form.get('factorial'):
            sonuc = math.factorial(int(num1))
            return render_template('index.html', sonuc=sonuc, num1=num1, num2=num2)
    
    
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)