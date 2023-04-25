from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from todo.forms import RegistrationForm,LoginForm,TaskForm,TaskUpdateForm,PasswordResetForm
from django.contrib.auth.models import User
from todo.models import Task
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"registration successfull")
    #         return redirect("signin")
    #     messages.error(request,"registration failed")
    #     return render(request,self.template_name,{"form":form})
    

class SignInView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfull")
                return redirect("task-list")
        messages.error(request,"login unsuccessfull")
        return render(request,self.template_name,{"form":form})
    


@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,self.template_name)
    



@method_decorator(signin_required,name="dispatch")
class TaskCreateView(CreateView):

    model=Task
    template_name="task-add.html"
    form_class=TaskForm
    success_url=reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"task created")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=self.form_class
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"task addedd successfully")
    #         return redirect("task-list")
    #     messages.error(request,"oops task add failed")
    #     return render(request,self.template_name,{"form":form})
    
@method_decorator(signin_required,name="dispatch")
class TaskListView(ListView):
    model=Task
    template_name="task-list.html"
    context_object_name="tasks"
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-created_date")
    # def get(self,request,*args,**kwargs):
    #     qs=Task.objects.filter(user=request.user).order_by("-created_date")
    #     return render(request,self.template_name,{"tasks":qs})
    
@method_decorator(signin_required,name="dispatch")
class TaskDetailView(DetailView):
    model=Task
    template_name="task-detail.html"
    context_object_name="task"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Task.objects.get(id=id)
    #     return render(request,self.template_name,{"task":qs})
    
@signin_required
def TaskDeleteView(request,*args,**kwargs):
    id=kwargs.get("pk")
    obj=Task.objects.get(id=id)
    if obj.user==request.user:
       Task.objects.get(id=id).delete()
       messages.success(request,"task removed")
       return redirect("task-list")
    else:
        messages.error(request,"you dont have the permission to do this")
        return redirect("signin")


@method_decorator(signin_required,name="dispatch")
class TaskUpdateView(UpdateView):
    model=Task
    template_name="task-edit.html"
    form_class=TaskUpdateForm
    # success_url=reverse_lazy("task-list")

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['pk']})
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     task=Task.objects.get(id=id)
    #     form=self.form_class(instance=task)
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     task=Task.objects.get(id=id)
    #     form=self.form_class(instance=task,data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"task updated successfully")
    #         return redirect("task-detail",pk=id)
    #     messages.error(request,"updation failed")
    #     return render(request,self.template_name,{"form":form})
    



def LogOutView(request,*args,**kwargs):
    logout(request)
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



