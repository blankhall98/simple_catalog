from flask import Flask, url_for,render_template,redirect
import os
import numpy as np
import pandas as pd

#self-made class
from inventory import Inventory
from store import Store

app = Flask(__name__)
app.config.secret_key = "xxxxxxxxxx"

@app.route('/')
def index():
    store = Store()
    inventory = Inventory()
    return render_template('index.html', store=store, inventory=inventory)

@app.route('/category/<cat_name>')
def category(cat_name):
    inventory = Inventory()
    cat_inv = inventory.inventory[cat_name]
    return render_template('category.html',cat_name = cat_name, inventory = inventory, cat_inv=cat_inv)

if __name__ == '__main__':
    app.run(debug=True)