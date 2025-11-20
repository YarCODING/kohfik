from flask import Flask, render_template, request
import psycopg2


site = Flask(__name__)

conn = psycopg2.connect(
        host="localhost",
        database="cafe",
        user='postgres',
        password='changeme'
        )
cur = conn.cursor()


query = """
SELECT * FROM public.customer;
"""
cur.execute(query)
print(cur.fetchall())
conn.commit()


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


if __name__ == "__main__":
    site.run(host='0.0.0.0', port=8000)