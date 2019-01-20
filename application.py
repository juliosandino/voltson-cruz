from flask import Flask
from flask import render_template
from vesync.api import VesynApi

app = Flask(__name__)

api = VesyncApi("jsandino@ucsc.edu", "porterbois")

app.config.update(
    TESTING=True,
    DEBUG=True
    )

@app.route("/")
def hello():
    api.get_devices()
    return render_template('index.html')

@app.route("/device/<cid>")
def show_user(cid):
    pass

if __name__ == "__main__":
    app.run()
