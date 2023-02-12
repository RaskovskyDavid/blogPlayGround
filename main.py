from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)    

@app.route('/')
def home():
    blog_url="https://api.npoint.io/ba1ee2b4217664c7159c"
    blog_response =requests.get(blog_url)
    all_post= blog_response.json()
    post_objects = []
    for post in all_post["articles"]:
        post_obj = Post(post["id"],post["title"],post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return render_template("index.html", all_posts=post_objects)
    
 
@app.route('/post/<int:index>')
def show_post(index):
    blog_url="https://api.npoint.io/ba1ee2b4217664c7159c"
    blog_response =requests.get(blog_url)
    all_post= blog_response.json()
    post_objects = []
    for post in all_post["articles"]:
            post_obj = Post(post["id"],post["title"],post["subtitle"], post["body"])
            post_objects.append(post_obj)        
    return render_template("post.html", all_posts=post_objects, num=index )

if __name__ == "__main__":
    app.run(debug=True)
