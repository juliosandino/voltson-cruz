from flask import Flask
from flask import render_template, url_for, redirect
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
    data = {}
    data['device'] = device
    data['cid'] = cid
    return render_template('device.html', data=data)

@app.route("/test/")
def test():
    devices = api.get_devices()
    data = {}
    data['devices'] = devices

    return render_template('test.html', data=data)

@app.route("/turn_on/<cid>")
def turn_on(cid):
    api.turn_on(cid)
    return 'success'

@app.route("/turn_off/<cid>")
def turn_off(cid):
    api.turn_off(cid)
    return render_template('turn_off_success.html')


if __name__ == "__main__":
    app.run()
