from django.shortcuts import render, redirect
from .models import Model
# Create your views here.
model = Model()
def index(request):
    return render(request, 'login/index.html')

def login(request):
    print(request.POST.get("username"))
    data = model.getUser({
        "username":request.POST.get("username"),
        "password":request.POST.get("password")
    }).getResult()
    print("DATANYA:")
    print(data)
    if data != None:
        if data['role'] == "admin":
            request.session['user_role_id'] = "admin"
        else:
            request.session['user_role_id'] = data['user_role_id']
        request.session['role'] = data['role']
        return redirect('/dashboard')
    return redirect("/login")

def logout(request):
    del request.session['user_role_id']
    del request.session['role']
    return redirect("/login")