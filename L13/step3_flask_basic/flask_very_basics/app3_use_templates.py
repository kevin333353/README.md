from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return ("Hello World")

@app.route("/showStatic/")
def showStatic():
    return app.send_static_file('myStaticPage.html')

@app.route("/useTemplates/<user>")
def useTemplates(user):
    return render_template('myTemplate.html',name=user)

if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)
