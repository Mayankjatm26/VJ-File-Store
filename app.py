from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run()

