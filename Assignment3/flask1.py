from flask import Flask
import requests 
import os

FLASK2_HOST="http://flask2:5002"

app=Flask(__name__)

if FLASK2_HOST==None :
    FLASK2_HOST="http://0.0.0.0:5002"

@app.route('/')
def hello():
    return 'Hello, This is Flask1'

@app.route('/<name>')
def hello_name(name):
    response=requests.get(FLASK2_HOST+f"/{name}")
    return response.text+' at Flask1'

if __name__ =='__main__' :
    app.run(host="0.0.0.0",port=5001)