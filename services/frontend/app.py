from flask import Flask, render_template

from common.health import bp
from common.logging_setup import setup_logger

app = Flask(__name__)
logger = setup_logger(app.import_name)
app.register_blueprint(bp)

@app.route("/")
def index():
    return render_template("tasks.html")
