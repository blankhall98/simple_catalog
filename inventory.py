import os
import numpy as np
import pandas as pd


class Inventory:

    def __init__(self):

        self.picture_path = './static/images/inventory/'
        self.inventory_path = './static/inventory.csv'
        self.category_reference = 'Clase'
        self.picture_reference = 'Imagen'
        self.inventory = {}
        self.load_inventory()

    def create_category(self,category_name):
        if not category_name in self.inventory:
            self.inventory[category_name] = {
                'products': [],
                'category_picture': ''
            }

    def read_inventory(self):
        token = pd.read_csv(self.inventory_path)
        return(token)

    def load_category(self,inventory,category_name,category_reference,picture_reference):
        token = []
        cat_db = inventory[inventory[category_reference] == category_name]
        cat_db.reset_index(drop=True, inplace=True)
        columns = cat_db.columns
        for prod in range(len(cat_db)):
            product = {}
            for col in columns:
                product[col] = cat_db[col][prod]
            token.append(product)
        self.inventory[category_name]['products'] = token
        self.inventory[category_name]['category_picture'] = token[0][picture_reference]

    def load_inventory(self):
        inventory = self.read_inventory()
        categories = inventory[self.category_reference].unique()
        for cat in categories:
            self.create_category(cat)
            self.load_category(inventory,cat,self.category_reference,self.picture_reference)

