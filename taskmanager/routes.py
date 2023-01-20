# Import render_template function for template rendering
from flask import render_template, request, redirect, url_for

# Import app and db variables from main taskmanager folder
from taskmanager import app, db

# Import models classes from models.py file
from taskmanager.models import Category, Task

# App route 
@app.route("/")
def home():
    return render_template("tasks.html")

# App route for categories.html
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

# App route for add_category.html
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", medthods=["GET", "POST"])
def edit_category(category_id):
    return render_template("edit_category.html")