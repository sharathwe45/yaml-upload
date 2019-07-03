import boto3
from flask import Flask, render_template, request, Response, jsonify, render_template_string
import yaml
import function_shield
import os

function_shield.configure({
    "policy": {        
        "outbound_connectivity": "block",
        "read_write_tmp": "block",
        "create_child_process": "block",
        "read_handler": "block"
    },
    "token": os.environ['FUNCTION_SHIELD_TOKEN']
})

app = Flask(__name__)

@app.route('/yaml_upload/', methods=['POST'])
def index():
    files = request.files['file']
    try:
        yaml_content = yaml.load(files)
        return str(yaml_content)        
    except Exception as e:
        return {"error": str(e)}
