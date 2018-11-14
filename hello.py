from typing import Optional

from flask import Flask, jsonify
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

    


app.run(port=5000)
