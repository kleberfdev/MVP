from django.shortcuts import render, redirect
from django.contrib.auth import logout


from .forms import UserForm, ItemForm
from .models import User, Item

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)

            # Verificar se é o usuário admin
            if username == 'admin' and password == 'admin':
                return redirect('admin_dashboard')  # Redirecionar para a página de cadastro

            request.session['user_id'] = user.id
            return redirect('home')
        except User.DoesNotExist:
            error_message = 'Usuário ou senha inválidos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificar se o usuário já existe
            if User.objects.filter(username=username).exists():
                error_message = 'O nome de usuário já está em uso.'
                return render(request, 'admin_dashboard.html', {'error_message': error_message})

            # Cadastrar o novo usuário
            user = User.objects.create(username=username, password=password)
            user.save()

            success_message = 'Usuário cadastrado com sucesso!'
            return render(request, 'admin_dashboard.html', {'success_message': success_message})

    # Se o formulário não for válido ou for uma solicitação GET, renderize a página de admin_dashboard.html
    return render(request, 'admin_dashboard.html')

def home_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = User.objects.get(id=user_id)
    items = Item.objects.filter(user=user)
    form = ItemForm(request.POST or None)  # Movido para cima
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
    # Aqui você pode adicionar qualquer lógica específica que deseja para a página de administração
    return render(request, 'admin_dashboard.html')

def create_order_view(request):
    # Implemente a lógica para criar um novo pedido aqui
    return render(request, 'create_order.html')

def show_users_view(request):
    # Implemente a lógica para mostrar a lista de pessoas cadastradas aqui
    users = User.objects.all()
    return render(request, 'show_users.html', {'users': users})