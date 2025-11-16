from flask import Flask, render_template, request
 

site = Flask(__name__)

# site.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:changeme@localhost/cafe'

@site.route("/", methods=['GET'])
def index():
    return render_template("index.html", title="home")

@site.route("/about", methods=['GET'])
def about():
    return render_template("about.html", title="About Us")

@site.route("/menu", methods=['GET'])
def menu():
    return render_template("menu.html", title="Menu")

@site.route("/blog", methods=['GET'])
def blog():
    return render_template("blog.html", title="Blog")

@site.route("/contact", methods=['GET'])
def contact():
    return render_template("contact.html", title="Contact Us")


site.run(host='0.0.0.0', port=8000)