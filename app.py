from flask import Flask, request
import json
from lightmngr import Lightmngr

app = Flask(__name__)
lightmngr = Lightmngr()


@app.route('/', methods=['PUT'])
def hello():
    cols = json.loads(request.data)
    lightmngr.set(cols)
    return "hello"
