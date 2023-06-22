from django.db import models
import json
import ast

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.TextField()
    lat_long = models.CharField(max_length=100)
    full_details = models.TextField()
    
    def __str__(self):
        return self.name
    def get_items(self):
        '''convert the items  from string to dictionary format'''
        items_dict = ast.literal_eval(self.items)
        return items_dict
