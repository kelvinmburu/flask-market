from flask import Flask, render_template

app = Flask(__name__) #Built-in variable that can be called for any variable file; can be called for any python file

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    return render_template('market.html')
