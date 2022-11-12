from flask import Flask,url_for, render_template
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)
@app.route("/")

def index():
    return render_template('index.html')
# return "Hello World, I'm Praveen..."
    





@app.route("/users/")

def profile1():
    return render_template('profile.html')
    
if __name__== "__main__":
    app.run()

# @app.route("/users/<username>")

# def profile(username):
#   return render_template('profile.html', username=username)