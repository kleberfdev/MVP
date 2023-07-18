from django.urls import path
from mvpapp import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home/')),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Nova rota para o painel de administração
    path('create_order/', views.create_order_view, name='create_order'),  # Nova rota para criar novo pedido
    path('show_users/', views.show_users_view, name='show_users'),  # Nova rota para mostrar pessoas cadastradas
]
