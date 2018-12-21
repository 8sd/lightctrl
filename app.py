from flask import Flask, request
import json
from lightmngr import Lightmngr

app = Flask(__name__)
lightmngr = Lightmngr()


@app.route('/', methods=['PUT'])
def setLight():
    cols = json.loads(request.data)
    lightmngr.set(cols)
    return "hello"


@app.route('/', methods=['GET'])
def getLight():
    return lightmngr.getReal()


@app.route('/speed', methods=['PUT'])
def setSpeed():
    lightmngr.speed = int(request.data)
