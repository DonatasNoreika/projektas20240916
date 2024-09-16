from flask import Flask
import flask_sqlalchemy

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Čia mano naujas superpuslapis</h1>"

if __name__ == "__main__":
    app.run(debug=True)