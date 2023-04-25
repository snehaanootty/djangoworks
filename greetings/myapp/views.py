from django.shortcuts import render
from django.views.generic import View
# Create your views here.
# localhost:8000/morning/
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"morning.html")
 
# localhost:8000/afternoon/
class GdAfternoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"afternoon.html")
    
# localhost:8000/night/
class GdnightView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"night.html")
    