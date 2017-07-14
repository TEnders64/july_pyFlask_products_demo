from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "asdfasdfasdf"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products', methods=['POST'])
def products():
    session['productName'] = request.form['productName']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)