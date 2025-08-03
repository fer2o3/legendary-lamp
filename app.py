from flask import Flask, render_template, Response
import random

app = Flask(__name__)

with open("quotes.txt", "r") as f:
    quotes = [line.strip() for line in f]

with open("people.txt", "r") as f:
    people = [line.strip() for line in f] 

def generate():
    quote = random.choice(quotes)
    person = random.choice(people)
    return f"{quote} - {person}"

@app.route("/")
def home():
    return render_template("index.html", message=generate())

@app.route("/index.txt")
def raw():
    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
