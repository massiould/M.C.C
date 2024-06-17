from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import  LoginForm, SignupForm,CheckForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import validate
from .models import Lawyer_identification
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.contrib.auth.models import User




@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print("Requête POST reçue")
        print(request.data)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Authentication successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        

        

@login_required
def index(request):
    return render(request, "index.html")


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                return redirect("check")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

@login_required
def check_lawyer(request):
    if request.method == "POST":
        form = CheckForm(request.POST)
        if form.is_valid():
            siren = form.cleaned_data['Siren']
            barreau = form.cleaned_data['Barreau']
            author = request.user
            if validate(siren, barreau,author) == True :
                return redirect("home")
    else:
        form = CheckForm()
    return render(request, "check.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("login")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})



