from flask import Flask, render_template, request
 

site = Flask(__name__)

@site.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@site.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@site.route("/menu", methods=['GET'])
def menu():
    return render_template("menu.html")

@site.route("/blog", methods=['GET'])
def blog():
    return render_template("blog.html")

@site.route("/contact", methods=['GET'])
def contact():
    return render_template("contact.html")


# site.run(host='localhost', port=8000)
site.run(host='0.0.0.0', port=8000)