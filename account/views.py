
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def home(request):
    if request.session.get("login"):
       return render(request, "index.html", {"login": True})
    else:
       return render(request, "index.html", {"login": False})

def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    if User.objects.filter(email=email, password=password).exists():
        u = User.objects.filter(email=email, password=password).get()
        request.session['login'] = True
        request.session["login_id"] = u.id
        return redirect(home)
    else:
        request.session['login'] = False
        print(request)
        return redirect(signin)

def signin(request):
    return render(request, "signin.html")

def jobber_signup(request):
    return render(request, "Jobber-Registration.html")

def customer_signup(request):
    return render(request, "User-Registration.html")

def create_jobber_account(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    address = request.POST["address"]
    password = request.POST["password"]
    pancard = request.POST["pancard"]
    photo = request.FILES["profile"]
    u = User(first_name=fname,last_name=lname,email= email, phone=phone, address= address,is_jobber=True,password= password, pan=pancard, profile_photo = photo)
    u.save()
    return redirect(signin)

def create_customer_account(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    address = request.POST["address"]
    password = request.POST["password"]
    u = User(first_name=fname,last_name= lname,email= email,address= address,is_jobber= True,password= password)
    u.save()
    return redirect(signin)

def profileView(request):
    u = User.objects.get(id = request.session["login_id"])
    return render(request, "profile-view.html", {"login": True, "user": u})

def logout(request):
    request.session["login"] = False
    request.session["login_id"] = ""
    return redirect(home)
