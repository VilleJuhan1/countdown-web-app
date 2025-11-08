from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

app = Flask(__name__)

@app.route("/")
def home():
    target_date = os.getenv("TARGET_DATE", "January 1, 2026 00:00:00")
    return render_template("index.html", target_date=target_date)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
