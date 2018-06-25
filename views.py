# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Menu, Items

def CreateData(request):
    breakfast = Menu(1,'Breakfast')
    i1 = Items(901,'poori',50, menu =breakfast)
    i2 = Items(902,'panni',60, menu =breakfast)
    cooldrink = Menu(2,'Cooldrink')
    i3 = Items(903,'pepsi',70, menu =cooldrink)
    i4 = Items(904,'coca',80,menu =cooldrink)
    icecream= Menu(3,'icecream')
    i5 = Items(905,'meetti',50, menu =icecream)
    i6 = Items(906,'vanilla',50,menu =icecream)
    

    breakfast.save()
    cooldrink.save()
    icecream.save()
    i1.save()
    i2.save()
    i3.save()
    i4.save()
    i5.save()
    i6.save()
    return render(request, "home.html")

def DisplayMenu(request):
    records =Menu.objects.all()
    return render(request,'display.html', {'record' : records})
def DeleteMenuWithItems(request):
    return render(request,'delete.html')
def RemoveMenuWithItems(request):
    menu_name = request.POST['t1']
    Menu.objects.get(name = menu_name).delete()
    return render(request,'home.html')

