# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
    Menu_Id =models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
class Items(models.Model):
    Item_Id =models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=20,decimal_places=2)
    menu = models.ForeignKey(Menu,on_delete = models.CASCADE)
