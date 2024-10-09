from flask import Flask

app = Flask(__name__)

@app.route("/") #創造實體
def hello_world():
    return "<h1>Hello, World!</h1>"

#gunicorn main(module名稱):app(WSGI應用程式名稱) #Ctrl+C中斷執行