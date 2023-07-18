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
            request.session['user_id'] = user.id
            return redirect('home')
        except User.DoesNotExist:
            error_message = 'Usuário ou senha inválidos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})

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
