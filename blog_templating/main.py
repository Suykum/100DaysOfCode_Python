from flask import Flask, render_template
import requests
from blog_templating.post import Post

app = Flask(__name__)
blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
all_post = requests.get(blog_url).json()
post_list = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_post]

@app.route('/')
def home():
    return render_template("index.html", posts=post_list)

@app.route('/blog/<int:index>')
def show_content(index):
    return render_template("post.html", post=post_list[index-1])

if __name__ == "__main__":
    app.run(debug=True)
