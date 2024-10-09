from flask import Flask

app = Flask(__name__)

@app.route("/") #創造實體 #gunicorn main(module名稱):app(應用程式名稱)
def hello_world():
    return "<h1>Hello, World!</h1>"