from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        user = request.form['name']
        return render_template('result.html', name=user)
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
