# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Menu, Items

admin.site.register(Menu)
admin.site.register(Items)
# Register your models here.