from typing import Optional

from flask import Flask, jsonify,request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hell0():
    return 'Hello, world'

@app.route('/employees')
def get_employees():
    url: str='https://employeewebapiazure20180822105822.azurewebsites.net/api/employees'
    response= requests.get(url)

    if(response.ok):
        content: Optional[bytes] = response.content
        jsonData: object = json.loads(content)
        data = jsonify({'employees' : jsonData})
        return data

    else:
        response.raise_for_status()


@app.route('/employees/<int:id>')
def get_employee_by_id(id):
    url= f'https://employeewebapiazure20180822105822.azurewebsites.net/api/employees/{id}'
    
    response= requests.get(url)
    
    if(response.ok):
        content= response.content
        jsonData: object= json.loads(content)
        return jsonify(jsonData)

    else:
        response.raise_for_status()



app.run(port=5000)
