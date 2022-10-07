from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(nome)
        print(email)
        print(password)
        
        if not nome.strip():
            print("Preencha corretamente1")

            return redirect('cadastro')
        
        if not email.strip():
            print("Preencha corretamente2")
            return redirect('cadastro')

        if password != password2:
            print("Senhas Divergentes!")
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print("Usuario já possui cadastro")
            return redirect('cadastro')

        user = User.objects.create_user(
        username=nome,
        email=email,
        password=password)
        
        user.save()
        
        print(f"{nome} Cadastrado com sucesso")
        print("Usuario cadastrado com sucesso!!!!")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("Dados incorretos")
            return redirect('login')
            
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print("Loogin realizado com sucesso")
        return redirect('index')
    return render(request, 'usuarios/login.html')


def logout(request):
  auth.logout(request)
  return redirect('index')