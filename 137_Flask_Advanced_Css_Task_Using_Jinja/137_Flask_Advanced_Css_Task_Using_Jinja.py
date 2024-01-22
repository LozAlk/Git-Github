# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
    # Render the homepage template with page title "h"
    return render_template("homepage.html",
                            title="Homepage",
                           custom_css="homepage")

@skills_app.route("/add")
def add():
    # Render the about page template with page title "D"
    return render_template("add.html",
                           title="Add Skills",
                           custom_css="add")



@skills_app.route("/about")
def about():
    # Render the about page template with page title "a"
    return render_template("about.html",title="About",)



if __name__ == "__main__":
    skills_app.run(debug=True, port=8000)
