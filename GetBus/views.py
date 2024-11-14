from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout




def home(request):
    return render(request,"index.html")



# Create Registeration Form Using UserCreationForms
def register(request):

    if request.method == "GET":
        form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
    return render(request,'register.html', {"form":form})


# Create Login Function using (authenticate,login,logout)
def userlogin(request):

    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # authenticate Function pass username and password if its valid it will return object if not None
        user = authenticate(username = username, password = password)

        # login function to login user on request
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')


# Create User Logout Function using logout
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login')