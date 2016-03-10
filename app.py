from flask import Flask, render_template, redirect, url_for
import subprocess
app = Flask(__name__)

raspistill_cmd = [
    "sudo",
    "raspistill",
    "--mode", "4",
    "-q", "80",
    "-w", "1296",
    "-h", "972",
    "--nopreview",
    "--ISO", "100",
    "--shutter", "16000",
    "--drc", "high",
    "--awb", "fluorescent",
    "--exposure", "night",
    "-o", "static/currentimg.jpg",
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/snap/")
def snap():
    subprocess.call(raspistill_cmd)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
