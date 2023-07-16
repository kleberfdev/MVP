from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .models import CustomUser
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')  # Redirecionar para a página inicial após o login bem-sucedido
        else:
            return render(request, 'accounts/login.html', {'error': 'Credenciais inválidas. Tente novamente.'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecionar para a página de login após o logout
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Processar o formulário e salvar o usuário no banco de dados
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Crie um novo objeto do modelo de usuário personalizado e salve-o no banco de dados
            user = CustomUser.objects.create_user(username=username, password=password)
            # Faça outras ações ou validações conforme necessário

            return redirect('accounts:login')  # Redirecione para a página de login após o registro bem-sucedido
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def home_view(request):
    # Coloque aqui a lógica para renderizar a página inicial
    return render(request, 'accounts/home.html')