from django.urls import path
# from django.contrib import admin
# from blearn_app.models import BoardModel

# from nbformat import read
from .views import signupfunc, loginfunc, listfunc, logoutfunc, BoardCreate, detailfunc
# goodfunc,readfunc, detailfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', BoardCreate.as_view(), name='create'),
]