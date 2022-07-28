from django.shortcuts import render, redirect
from .models import Usuarios
from hashlib import sha256

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def validar_cadastro(request):
    #Status 0 = Usuário cadastrado com sucesso
    #Status 1 = Usuário e email não podem estar vazios 
    #Status 2 = Sua senha deve ter mais de 8 caracteres
    #Status 3 = Email já cadastrado
    #Status 4 = Erro interno do sistema
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuarios.objects.filter(email=email)


    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('auth/cadastro/?status=2')

    if usuario:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuarios(nome=nome,
                           email=email,
                           senha=senha)
        usuario.save()
        return redirect('/auth/login/?status=0')

    except:
        return redirect('/auth/cadastro/?status=4')

def validar_login(request):
    return render(request, 'login.html')


