from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>外星幽靈貓貓,您好!</h1>" #修改後終端機必須關掉重啟才會更改

#flask開發測試版(修改後網頁重整就好):flask --app main1(module名稱) run --debug