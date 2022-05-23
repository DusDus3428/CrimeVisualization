from gatherer import app
from flask import request
import json


@app.post('/target')
def select_target_api():
    target_api = request.json
    