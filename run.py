import datetime
import os
import time

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_heaven'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


# Home page route
@app.route('/')
def home_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())


# Recipe page route
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


# Add recipe form
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    meal=mongo.db.meal.find())


# Add submit recipe form
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


# Edit recipe form
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_meal =  mongo.db.meal.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           meal=all_meal)


# Update submit recipe form
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'title':request.form.get('title'),
        'description':request.form.get('description'),
        'directions':request.form.get('directions'),
        'ingredients':request.form.get('ingredients'),
        'meal_type':request.form.get('meal_type'),
        'serves':request.form.get('serves'),
        'cooking_time':request.form.get('cooking_time'),
        'prep_time':request.form.get('prep_time'),
        'cuisine':request.form.get('cuisine'),
        'user_name':request.form.get('user_name'),
        'last_modified': time.asctime(time.localtime(time.time()))
    })
    return redirect(url_for('get_recipes'))


# Delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# Single page recipe
@app.route('/recipe_single/<recipe_id>')
def recipe_single(recipe_id):
    return render_template("recipepage.html",
                           recipes=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
                           


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False)