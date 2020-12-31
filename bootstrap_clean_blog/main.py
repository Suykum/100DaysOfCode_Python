from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/43644ec4f0013682fc0d"
all_post = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html", post=all_post[id-1])


if __name__ == "__main__":
    app.run(debug=True)