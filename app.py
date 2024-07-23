from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # Home page
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) # '0.0.0.0' to run locally 