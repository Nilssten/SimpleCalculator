from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Nevar dalīt ar nulli"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
    except ValueError:
        return render_template('index.html', result="Ievadi skaitli!")

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return render_template('index.html', result="Nederīga operācija!")

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)