from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        senha_confirma = request.POST.get('senha_confirma')
        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request,constants.WARNING,'Usuario já cadastrado!')
            return redirect('/usuarios/cadastro')
        
        if len(username) < 3:
            messages.add_message(request,constants.WARNING,'Usuario deve conter 3 caracteres ou mais!')
            return redirect('/usuarios/cadastro')
        
        if senha != senha_confirma:
            messages.add_message(request,constants.ERROR,'As senhas não são iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request,constants.WARNING,'A senha deve conter 6 caracteres ou mais!')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.create_user(
            username=username,
            password=senha
        )
        return redirect('/usuarios/logar')

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/home') # Vai dar erro

        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/logar')