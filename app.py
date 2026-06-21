from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/projects')
def projects():
    return "Projects Module"

@app.route('/labours')
def labours():
    return "Labours Module"

@app.route('/materials')
def materials():
    return "Materials Module"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
