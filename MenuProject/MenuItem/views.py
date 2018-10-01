# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Menu, Items


from django.http import  HttpResponse

def CreateData(request):
    breakfast = Menu(1,'Breakfast')
    i1 = Items(901,'poori',50.00, menu =breakfast)
    i2 = Items(902,'alubada',60, menu =breakfast)
    i3 = Items(903,'kachodi',10, menu =breakfast)
    i4= Items(904,'Samosa',10, menu =breakfast)
    cooldrink = Menu(2,'Cooldrink')
    i5 = Items(905,'pepsi',70, menu =cooldrink)
    i6 = Items(906,'coca',80,menu =cooldrink)
    i7 = Items(907,'thumps',10, menu =cooldrink)
    i8 = Items(908,'water',70, menu =cooldrink)
    icecream= Menu(3,'icecream')
    i9 = Items(909,'meetti',50, menu =icecream)
    i10 = Items(910,'vanilla',50,menu =icecream)
    

    breakfast.save()
    cooldrink.save()
    icecream.save()
    i1.save()
    i2.save()
    i3.save()
    i4.save()
    i5.save()
    i6.save()
    i7.save()
    i8.save()
    i9.save()
    i10.save()
    return render(request, "home.html")

def DisplayMenu(request):
    records =Menu.objects.all()
    return render(request, 'display.html', {'records' : records})
def DeleteMenuWithItems(request):
    return render(request, 'delete.html')
def RemoveMenuWithItems(request):
    if request.method == 'POST':
    menu_name = request.POST['t1']
    removed_item = Menu.objects.filter(name=menu_name).delete()
    return redirect('display')
    #print(request.post)

