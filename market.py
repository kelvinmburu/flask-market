from flask import Flask, render_template

app = Flask(__name__) #Built-in variable that can be called for any variable file; can be called for any python file

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
        {'id':1, 'name': 'Phone', 'barcode':'95575949487839','price':500},
        {'id':2, 'name': 'Laptop', 'barcode':'955759497365242','price':700},
        {'id':3, 'name': 'Tablet', 'barcode':'9573902435936','price':900}
    ]
    return render_template('market.html', items=items)
