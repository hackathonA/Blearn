from django.urls import path, include
# from django.contrib import admin


from .views import signupfunc, loginfunc, listfunc, logoutfunc, BoardCreate, detailfunc


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('auth/', include('social_django.urls', namespace='social'))
]