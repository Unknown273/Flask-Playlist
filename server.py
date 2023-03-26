from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "fn208g02"

@app.route("/")
def hello():
  return "Hello"

@app.route("/about")
def about():
  return "The about page"

@app.route("/blog")
def blog():
  posts = [
    {"title": "Technology in 2019", "author": "Avi"},
    {"title": "Expansion of Oil in Russia", "author": "Bob"}
  ]
  return render_template('blog.html', author="Yusuf Kazi", weather="rainy", posts=posts)

@app.route("/blog/<int:blog_id>")
def blogpost(blog_id):
  return f"This my blog number {blog_id}"

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignUpForm()
  if form.is_submitted():
    result = request.form
    return render_template("user.html", result=result)
  return render_template('signup.html', form=form)

if __name__ == "__main__":
  app.run()