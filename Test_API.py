import json
from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/Test', methods=["POST"])
def Test():
    data=request.json
    print(data)
    return json.dumps("Succesful post")
app.run()