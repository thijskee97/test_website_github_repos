from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'





@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route("/work-single.html")
def work():
    return render_template("work-single.html")

@app.route("/work-single2.html")
def work2():
    return render_template("work-single2.html")


@app.route("/work-single3.html")
def work3():
    return render_template("work-single3.html")

@app.route("/work-single4.html")
def work4():
    return render_template("work-single4.html")

@app.route("/work-single5.html")
def work5():
    return render_template("work-single5.html")

@app.route("/work-single6.html")
def work6():
    return render_template("work-single6.html")

if __name__ == "__main__":
    app.run(debug=True)