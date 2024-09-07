from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, BAKU!</h1>"

@app.route('/about/<altay>')
def about_page(altay):
    return f"<h1>Hello, {altay}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
