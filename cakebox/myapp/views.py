from django.shortcuts import render,redirect
from django.views.generic import View
from django import forms
from myapp.models import Cake
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# class CakeForm(forms.Form):
#     name=forms.CharField()
#     flavour=forms.CharField()
#     price=forms.IntegerField()
#     shape=forms.CharField()
#     weight=forms.CharField()
#     layer=forms.IntegerField()
#     description=forms.CharField()

class CakeForm(forms.ModelForm):
    class Meta:
        model=Cake
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "shape":forms.Select(attrs={"class":"form-select"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "pic":forms.FileInput(attrs={"class":"form-control"})

        }

class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

   

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"cake-register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user registered successfully")
            return redirect("signin")
        messages.error(request,"user registration failed")
        return render(request,"cake-register.html",{"form":form})
    
def signout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logouted")
    return redirect("signin")
    

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)

                messages.success(request,"login succesfull")
                return redirect("cakelist")
        messages.error(request,"oops!! there is a trouble while login")
        return render(request,"signin.html",{"form":form})

class CakeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm()
        return render(request,"cake-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=CakeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"cake created")
            return redirect("cakelist")
        messages.error(request,"cake creation failed")
        return render(request,"cake-add.html",{"form":form})
    
class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Cake.objects.all()
        return render(request,"cake-list.html",{"cakes":qs})
    

class CakeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cake.objects.get(id=id)
        return render(request,"cake-detail.html",{"cake":qs})


class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cake.objects.filter(id=id).delete()
        messages.success(request,"cake deleted")
        return redirect("cakelist")
    

class CakeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp=Cake.objects.get(id=id)
        form=CakeForm(instance=emp)
        return render(request,"cake-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp=Cake.objects.get(id=id)
        form=CakeForm(data=request.POST,instance=emp,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"cake updated successfully")
            return redirect('cakedetail',pk=id)
        messages.error(request,"cake updation failed")
        return render(request,"cake-edit.html",{"form":form})