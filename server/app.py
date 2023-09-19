from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # Print the string to the console
    return input_string  # Display it in the web browser

@app.route('/count/<int:parameter>')
def count(parameter):
    parameter = 'num'.join((str) (i) for i in range(parameter ))+ '0'
    return parameter

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)  # Try to convert to int
    except ValueError:
        try:
            num1 = float(num1)  # If it's not an int, try to convert to float
        except ValueError:
            return "Invalid input for num1"

    try:
        num2 = int(num2)  # Try to convert to int
    except ValueError:
        try:
            num2 = float(num2)  # If it's not an int, try to convert to float
        except ValueError:
            return "Invalid input for num2"

    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, %"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



