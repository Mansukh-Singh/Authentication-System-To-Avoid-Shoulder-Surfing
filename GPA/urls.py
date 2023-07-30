from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
    path('revise/',views.revise,name = 'revise'),
    path('page/',views.page,name = 'page'),
    path('email/',views.email,name = 'email'),
]