from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello"

@app.route("/about")
def about():
  return "The about page"

@app.route("/blog")
def blog():
  return render_template('blog.html', author="Yusuf Kazi")

@app.route("/blog/<int:blog_id>")
def blogpost(blog_id):
  return f"This my blog number {blog_id}"

if __name__ == "__main__":
  app.run()