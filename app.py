from flask import Flask
from flask import request
import json

from data import data

app = Flask(
    __name__,
    static_folder="static",         # 放靜態資料的資料夾
    static_url_path="/static"       # 可以存取資料夾內檔案的連結
    )

@app.route("/")                     # 點進localhost:3000就執行
def hello():
    return "Hello, World!"

@app.route("/data")                 # 在localhost:3000/data執行
def getData():
    nums = int(request.args.get("num", len(data)))      # 可以用localhost:3000/data?num=...來設定要拿多少資料
    
    if nums > len(data):
        return "我們最多只有這些<br>"+ json.dumps(data, ensure_ascii=False)
    
    return json.dumps([data[i] for i in range(nums)], ensure_ascii=False)   # 回傳json
    
if __name__ == "__main__":
    app.run(port=3000)