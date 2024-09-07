from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('home.html')

@app.route('/about/<altay>')
def about_page(altay):
    return f"<h1>Hello, {altay}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
