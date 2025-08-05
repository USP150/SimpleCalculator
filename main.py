from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculator', methods=['POST'])
def calculator():
    try:
        data = request.form
        x = float(data['x'])  # safer than eval
        y = float(data['y'])
        operation = data['operation']

        if operation == 'addition':
            result = x + y
        elif operation == 'subtraction':  # corrected spelling
            result = x - y
        elif operation == 'multiplication':
            result = x * y
        elif operation == 'division':
            if y == 0:
                return jsonify({"status": "error", "message": "Cannot divide by zero"})
            result = x / y
        else:
            return jsonify({"status": "error", "message": "Invalid operation"})

        return jsonify({"status": "success", "result": result})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
