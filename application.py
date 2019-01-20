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
def show_user(cid):
    pass

if __name__ == "__main__":
    app.run()
