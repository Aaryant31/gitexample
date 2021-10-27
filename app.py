from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello world"


@app.route('/predict')
def predict():
    a= 0
    return "prediction : Rahul Soni is very good data scientist"