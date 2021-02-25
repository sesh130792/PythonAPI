# To view the PUT and DELETE method changes:
# New record -: curl -i -H "Content-Type: Application/json" -X POST http://127.0.0.1:5000/employees
# update existing record -: curl -i -H "Content-Type: Application/json" -X PUT http://127.0.0.1:5000/employees/2
# remove a record -: curl -i -H "Content-Type: Application/json" -X DELETE http://127.0.0.1:5000/employees/3

from flask import Flask, jsonify

app = Flask(__name__)


Employees = [{'name': 'Arun', 'id': 1, 'age': 28},
             {'name': 'Bhargav', 'id': 2, 'age': 24},
             {'name': 'Chandru', 'id': 3, 'age': 30},
             {'name': 'Dinesh', 'id': 4, 'age': 29}]


@app.route('/')
def index():
    return "Welcome to my rest api!!"


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({'Employees': Employees})


@app.route('/employee/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    return jsonify({'Employees': Employees[id-1]})


@app.route('/employees', methods=['POST'])
def create_new_employee():
    emp = {'name': 'Raja', 'id': 5, 'age': 30}
    Employees.append(emp)
    return jsonify({'Created': Employees})


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee_detail(id):
    Employees[id]['age'] = 30
    return jsonify({'Employees': Employees})


@app.route('/employees/<int:id>', methods=['DELETE'])
def remove_employee(id):
    Employees.remove(Employees[id])
    return jsonify({'Updated': Employees})


if __name__ == "__main__":
    app.run(debug=True)