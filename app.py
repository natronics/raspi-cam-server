from flask import Flask, render_template, redirect, url_for
import subprocess
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/snap/")
def snap():
    subprocess.call(["raspistill", "-o", "static/currentimg.jpg"])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
