from django.urls import path
from mvpapp import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home/')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('logout/', views.logout_view, name='logout'),
]
