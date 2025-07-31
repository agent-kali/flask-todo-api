from flask import Flask, jsonify, request
print("Файл запущен!")
app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todos.append(data)
    return jsonify({"message": "Todo added!", "todo": data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)