from flask import Flask
import os

app = Flask(__name__)

print(os.environ["USERNAME"])
print(os.environ["PASSWORD"])

@app.route("/", methods=["GET"])
def home():
    return "test"

if __name__ == "__main__":
    app.run()
