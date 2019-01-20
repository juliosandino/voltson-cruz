from flask import Flask
from flask import render_template
app = Flask(__name__)

app.config.update(
    TESTING=True,
    DEBUG=True
    )

@app.route("/")
def hello():
    return render_template('base.html')

if __name__ == "__main__":
    app.run()
