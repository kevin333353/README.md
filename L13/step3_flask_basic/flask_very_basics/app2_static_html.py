from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return ("Hello World")

@app.route("/showStatic/")
def showStatic():
    return app.send_static_file('myStaticPage.html')


if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)
