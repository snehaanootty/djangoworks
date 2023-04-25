from django.shortcuts import render
from django.views.generic import View
from django import forms


from geopy.geocoders import Nominatim
 
def get_address(place):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
    return getLoc.address

class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()


class Geoform(forms.Form):
    place=forms.CharField()


class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1+n2
        print(res)
        return render(request,"add.html",{"result":res})
    

class SubtractView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"subtract.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("numb1"))
        n2=int(request.POST.get("numb2"))
        res=n1-n2
        print(res)
        return render(request,"subtract.html",{"result":res})
    

class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"multi.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     n1=int(request.POST.get("num1"))
    #     n2=int(request.POST.get("num2"))
    #     res=n1*n2
    #     print(res)
    def post(self,request,*args,**kwargs):
        print(request.POST)
        form=OperationForm(request.POST)
        if form.is_valid():
            print("form valid")
        else:
            print("form invalid")
        return render(request,"multi.html")
    

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"divide.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     n1=int(request.POST.get("num1"))
    #     n2=int(request.POST.get("num2"))
    #     res=n1/n2
    #     print(res)
    #     return render(request,"divide.html",{"result":res})
    def post(self,request,*args,**kwargs):
        print(request.POST)
        form=OperationForm(request.POST)
        if form.is_valid():
            print("form valid")
        else:
            print("form invalid")
        return render(request,"divide.html")
    
class factorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        fact=1
        for i in range(1,(n+1)):
            fact=fact*i
        return render(request,"fact.html",{"result":fact})
    
class primenumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        f=0
        if n==1:
            res=("not defined")
        else:
            for i in range(1,(n+1)):
                if(n%i==0):
                    f=f+1
        if f==2:
            res=("prime")
        else:
            res=("not prime")
        return render(request,"prime.html",{"result":res})
    
class armstrongView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"armstrong.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        ln=len(n)
        sum=0
        n=int(n)
        temp=n
        while(temp>0):
            r=temp%10
            sum=sum+r**ln
            temp=temp//10
        if n==sum:
            res=("Armstrong")
        else:
            res=("not armstrong")

        return render(request,"armstrong.html",{"result":res})
    

class palindromView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"palindrom.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        rev=0
        temp=n
        while(temp>0):
            r=temp%10
            rev=rev*10+r
            temp=temp//10
        if(n==rev):
            res=("palindrom")
        else:
            res=("not palindrom")
        return render(request,"palindrom.html",{"result":res})
    

class rangeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"range.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        evens=[ i for i in range(n1,n2) if i%2==0]
        return render(request,"range.html",{"result":evens})
    
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class HealthView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"health.html")
    def post(self,request,*args,**kwargs):
        tummy=int(request.POST.get("tummy"))
        buttock=int(request.POST.get("buttock"))
        gender=request.POST.get("gender")
        bmi=tummy/buttock
        bmi=round(bmi,2)
        context={"gender":"","risk":"","shape":"","bmi":bmi}
        if gender=="male":
            if bmi<=.95:
                context["gender"]="male"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi>=.95 and bmi<=1:
                context["gender"]="male"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi>1:
                context["gender"]="male"
                context["risk"]="high"
                context["shape"]="apple"
        else:
            if bmi<=.80:
                context["gender"]="female"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi>=.81 and bmi<=.85:
                context["gender"]="female"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi>.85:
                context["gender"]="female"
                context["risk"]="high"
                context["shape"]="apple"

        return render(request,"health.html",context)
    
class TemparatureView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"temparature.html")
    def post(self,request,*args,**kwargs):
        temp=int(request.POST.get("temp"))
        result=(temp * 9/5) + 32 
        return render(request,"temparature.html",{"result":result})
    

class ExponentView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
    def post(self,request,*args,**kwargs):
        print(request.POST)
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1**n2
        return render(request,"exponent.html",{"result":result,"form":form})
    
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"loginform":form})
    

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"register":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("invalid form")
        return render(request,"registration.html",{"register":form})
    
class geoView(View):
    def get(self,request,*args,**kwargs):
        form=Geoform()
        return render(request,"geo.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Geoform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            place=form.cleaned_data.get("place")
            address=get_address(place)
            print(address)
        else:
            print("invalid")
        return render(request,"geo.html",{"form":form,"result":address})


class LocationForm(forms.Form):
    lattitude=forms.IntegerField()
    longitude=forms.IntegerField()


from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("kakkanad india")
print(getLoc.address)

print("getLoc.latitude")
print("getLoc.longitude")





class LocationView(View):
    def get(self,request,*args,**kw):
        form=LocationForm()
        return render(request,"location.html",{"form":form})
    def post(self,request,*args,**kw):
        form=LocationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            l1=form.cleaned_data.get("lattitude")
            l2=form.cleaned_data.get("longitude")
             
            Address=(getLoc.address)
        return render(request,"location.html",{"form":form,"result":Address})
