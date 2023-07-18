from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .forms import UserForm, ItemForm
from .models import Item

User = get_user_model()

# Restante das views...


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserForm, ItemForm
from .models import User, Item

def login_view(request):
    print("Request Method:", request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            print("User authenticated successfully.")  # Adicione esta linha para depurar
            login(request, user)

            if user.username == 'admin':
                print("Redirecting to admin_dashboard.")  # Adicione esta linha para depurar
                return redirect('admin_dashboard')

            print("Redirecting to home.")  # Adicione esta linha para depurar
            return redirect('home')

        error_message = 'Usuário ou senha inválidos.'
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def home_view(request):
    user = request.user
    items = Item.objects.filter(user=user)
    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = user
            item.save()
            return redirect('home')

    return render(request, 'home.html', {'user': user, 'items': items, 'form': form})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('home')

def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_item.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
def admin_dashboard(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificar se o usuário já existe no modelo de usuário padrão
            if User.objects.filter(username=username).exists():
                error_message = 'O nome de usuário já está em uso.'
                return render(request, 'admin_dashboard.html', {'form': form, 'error_message': error_message})

            # Cadastrar o novo usuário usando o gerenciador de autenticação padrão
            user = User.objects.create_user(username=username, password=password)
            user.save()

            success_message = 'Usuário cadastrado com sucesso!'
            return render(request, 'admin_dashboard.html', {'form': form, 'success_message': success_message})

    else:
        # Se não for uma solicitação de POST, exiba a página de administração com o formulário de cadastro de usuário vazio
        form = UserForm()

    # Obtenha a lista de pessoas cadastradas do modelo de usuário padrão
    users = User.objects.all()

    return render(request, 'admin_dashboard.html', {'form': form, 'users': users})

def create_order_view(request):
    # Implemente a lógica para criar um novo pedido aqui
    return render(request, 'create_order.html')

def show_users_view(request):
    # Implemente a lógica para mostrar a lista de pessoas cadastradas aqui
    users = User.objects.all()
    return render(request, 'show_users.html', {'users': users})