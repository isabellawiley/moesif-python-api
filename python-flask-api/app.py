import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [ {'id': 1, 'name': 'Bob'}, {'id': 2, 'name': 'Tom'}, {'id': 3, 'name': 'Thor'}]

nextEmployeeId = 4

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
    return True