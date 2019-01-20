from flask import Flask
from flask import render_template
from vesync.api import VesyncApi

app = Flask(__name__)

api = VesyncApi("jsandino@ucsc.edu", "porterbois")

app.config.update(
    TESTING=True,
    DEBUG=True
    )

@app.route("/")
def hello():
    devices = api.get_devices()
    information = {}
    information['devices'] = devices

    return render_template('index.html', information=information)

@app.route("/device/<cid>")
def device(cid):
    device = api.get_detail(cid)
    return render_template('device.html', device=device)

@app.route("/test/")
def test():
    devices = api.get_devices()
    information = {}
    information['devices'] = devices

    return render_template('test.html', information=information)

if __name__ == "__main__":
    app.run()
