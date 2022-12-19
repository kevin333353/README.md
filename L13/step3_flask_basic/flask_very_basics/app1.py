from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return ("Hello World")

@app.route("/show/")
def add():
    return ("show text only")


if __name__ == "__main__":
    app.run()
