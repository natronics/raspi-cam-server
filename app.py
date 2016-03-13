from flask import Flask, render_template, redirect, url_for
import subprocess
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import json

app = Flask(__name__)

raspistill_cmd = [
    "sudo",
    "raspistill",
    "--mode", "4",
    "-q", "80",
    "-w", "1296",
    "-h", "972",
    "--nopreview",
#    "--ISO", "100",
#    "--shutter", "16000",
#    "--drc", "high",
    "--awb", "fluorescent",
#    "--exposure", "night",
    "-o", "static/currentimg.jpg",
]

flir_cmd = ["sudo", "raspberrypi_capture"]


@app.route("/")
def index():
    return render_template('index.html', now=datetime.datetime.now())


@app.route("/snap/")
def snap():
    subprocess.call(raspistill_cmd)
    subprocess.call(flir_cmd)

    with open('IMG_0000.json') as f:
        data = json.loads(f.read())['image']

    fig = plt.figure(frameon=False)
    fig.set_size_inches(4,3)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(data, cm.inferno, interpolation="bicubic", vmin=7400, vmax=7700)
    plt.savefig("static/currentflir.png", dpi=250)

    subprocess.call("mv -f IMG_0000.json static/currentflir.json", shell=True)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
