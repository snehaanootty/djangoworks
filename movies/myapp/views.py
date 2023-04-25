from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,ListView,CreateView,UpdateView,DetailView
from myapp.forms import RegistrationForm,LoginForm,MovieForm,PasswordResetForm
from django.contrib.auth.models import User
from myapp.models import Movie
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not  request.user.is_authenticated:
            messages.error(request,"you must login!!")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper


class SignUpView(CreateView):
    model=User
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
     
    def form_valid(self, form):
        messages.success(self.request,"accounted created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)


class signInView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
           
                messages.success(request,"login successfull")
                return redirect("index")
            messages.error(request,"can't login")
            return render(request,self.template_name,{"form":form})


class MovieAddView(View):
    model=Movie
    template_name="movie-add.html"
    form_class=MovieForm
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movie-list")
        return render(request,self.template_name,{"form":form})

#     # def form_valid(self, form):
#     #     form.instance.user=self.request.user
#     #     messages.success(self.request,"task created")
#     #     return super().form_valid(form)
    
    
        
@method_decorator(signin_required,name="dispatch")
class MovieListView(ListView):

    model=Movie
    template_name="movie-list.html"
    context_object_name="movies"
   


    # def get(self,request,*args,**kwargs):
    #     qs=Movie.objects.all()
    #     return render(request,self.template_name,{"movies":qs})
    

@method_decorator(signin_required,name="dispatch")
class MovieDetailView(DetailView):
    model=Movie
    template_name="movie-detail.html"
    context_object_name="movie"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Movie.objects.get(id=id)
    #     return render(request,self.template_name,{"movie":qs})
    
@method_decorator(signin_required,name="dispatch")   
class MovieUpdateView(UpdateView):
    model=Movie
    template_name="movie-edit.html"
    form_class=MovieForm
    success_url=reverse_lazy("movie-list")


    # def get_success_url(self):
    #     return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['pk']})

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     movie=Movie.objects.get(id=id)
    #     form=self.form_class(instance=movie)
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     movie=Movie.objects.get(id=id)
    #     form=self.form_class(instance=movie,data=request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"movie details updated")
    #         return redirect("movie-detail",pk=id)
    #     messages.error(request,"movie cant update")
    #     return render(request,self.template_name,{"form":form})
    

@signin_required
def MovieDeleteView(request,*args,**kwargs):
    id=kwargs.get("pk")
    movie=Movie.objects.get(id=id).delete()
    messages.success(request,"movie deleted")
    return redirect("movie-list")

@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,self.template_name)
    
@signin_required
def LogOutView(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logout successfull")
    return redirect("signin")


class PasswordResetView(FormView):
    model=User
    template_name="password-reset.html"
    form_class=PasswordResetForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            pwd1=form.cleaned_data.get("password1")
            pwd2=form.cleaned_data.get("password2")

            if pwd1==pwd2:
               
                try:
                   
                    usr=User.objects.get(username=username,email=email)
                    usr.set_password(pwd2)
                    usr.save()
                    messages.success(request,"password changed")
                    return redirect("signin")
                except Exception as e:
                    messages.error(request,"invalid credemtials")
                    return render(request,self.template_name,{"form":form})
            else:
                messages.error(request,"password mismatch")
                return render(request,self.template_name,{"form":form})



