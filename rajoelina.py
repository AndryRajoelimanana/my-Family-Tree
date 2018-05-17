from flask import Flask, render_template
import os, json
app = Flask(__name__)

@app.route('/')
def index():
    data = json.load(open("templates/data.json"))
    return render_template("index.html", data=data)
    

if __name__ == '__main__':
    app.run(debug=True, threaded = True)
