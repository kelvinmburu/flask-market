from flask import Flask, render_template

app = Flask(__name__) #Built-in variable that can be called for any variable file; can be called for any python file

@app.route("/")
def home_page():
    return render_template('home.html')
