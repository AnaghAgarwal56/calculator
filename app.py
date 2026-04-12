from flask import Flask, render_template, request, redirect

app = Flask(__name__)

history = []

@app.route('/')
def index():
    return render_template('index.html', result=None, num1='', num2='', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
            op = '+'
        elif operation == 'subtract':
            result = num1 - num2
            op = '-'
        elif operation == 'multiply':
            result = num1 * num2
            op = '*'
        elif operation == 'divide':
            if num2 == 0:
                return render_template('index.html', result="Cannot divide by zero", num1=num1, num2=num2, history=history)
            result = num1 / num2
            op = '/'
        elif operation == 'power':
            result = num1 ** num2
            op = '^'

        expression = f"{num1} {op} {num2} = {result}"
        history.append(expression)

    except:
        return render_template('index.html', result="Invalid input", num1='', num2='', history=history)

    return render_template('index.html', result=result, num1=num1, num2=num2, history=history)


# 🔹 1. Clear inputs + result
@app.route('/clear')
def clear():
    return redirect('/')


# 🔹 2. Clear full history
@app.route('/clear_history')
def clear_history():
    history.clear()
    return redirect('/')


# 🔹 3. Delete single history item
@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(history):
        history.pop(index)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
