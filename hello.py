from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell0():
    return 'Hello, world'

@app.route('/employees')
def get_employees():
    pass

app.run(port=5000)
