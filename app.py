from flask import Flask
from flask import request
import json

from data import data

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
    )

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/data")
def getData():
    nums = int(request.args.get("num", len(data)))
    
    if nums > len(data):
        return "我們最多只有這些<br>"+ json.dumps(data, ensure_ascii=False)
    
    return json.dumps([data[i] for i in range(nums)], ensure_ascii=False)
    
if __name__ == "__main__":
    app.run(port=3000)