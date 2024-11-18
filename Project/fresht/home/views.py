from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import movies
from .models import movies_hollywood
from .models import movies_surprises
from .models import movies_theatre
from .models import search
from .forms import *
from django.contrib.auth.models import User
import pdb


def home(request):
    if request.method == "GET":
        return render(request, "Main.html",context={"ctx":movies.objects.all().values(),"ctx_theatre":movies_theatre.objects.all().values(),"ctx_hollywood":movies_hollywood.objects.all().values(),"ctx_surprises":movies_surprises.objects.all().values()})
    if request.method == "POST":
        search_name=request.POST["movie_name"]
        n=-1
        for i in movies.objects.all().values_list("name"):
            n=n+1
            if i[0]==search_name:
                return render(request, "Review.html", context={"ctx":movies.objects.all().values()[int(n)],"reviews":user_review.objects.all().values()})

class review_page(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context={"ctx":movies.objects.all().values()[int(n)],"reviews":user_review.objects.all().values()})

class review_page_theatre(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context={"ctx":movies_theatre.objects.all().values()[int(n)],"reviews":user_review.objects.all().values()})
    
class review_page_hollywood(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context={"ctx":movies_hollywood.objects.all().values()[int(n)],"reviews":user_review.objects.all().values()})
    
class review_page_surprises(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context={"ctx":movies_surprises.objects.all().values()[int(n)],"reviews":user_review.objects.all().values()})
    
def signup(request):
    if request.method == "POST":
            username = request.POST['username']
            user_name = username
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username already exists.')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('Email already registered.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            return render(request,"Main.html",context={"ctx":movies.objects.all().values(),"ctx_theatre":movies_theatre.objects.all().values(),"ctx_hollywood":movies_hollywood.objects.all().values(),"ctx_surprises":movies_surprises.objects.all().values()})
                
    form=dump_user_info
    return render(request,"signup.html",context={"form":form})

class user_review_page(View):
    form=dump_user_review
    def post(self,request,n=None,m=None):
        form=dump_user_review(request.POST)
        if form.is_valid():
            form.cleaned_data.update({"slug":m})
            form.cleaned_data.update({"vno":n})
            new_form=dump_user_review(form.cleaned_data)
            new_form.save()
        return redirect('/')
    def get(self,request,n=None,m=None):
        if int(n)==1:
            ctx=movies.objects.all().values()[int(m)]
        elif int(n)==2:
            ctx=movies_theatre.objects.all().values()[int(m)]
        elif int(n)==3:
            ctx=movies_hollywood.objects.all().values()[int(m)]
        elif int(n)==4:
            ctx=movies_surprises.objects.all().values()[int(m)]
        return render(request, "user_review.html", context={"ctx":ctx,"form":self.form})
    