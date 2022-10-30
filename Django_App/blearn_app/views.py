from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blearn_app.models import BoardModel
# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,'',password)
            return redirect('login')
        except IntegrityError:
            return render(request,'signup.html', {'error':'このユーザーはすでに登録されています'})
    # return redirect('login')
    return render(request, 'signup.html')
             
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create')
        else:
            # return render(request,'signup.html', {})
            return  redirect('signup')
    return render(request,'login.html', {})
    
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})
    # object = get_object_or_404(User, pk=pk)
    # return render(request, 'list.html', {'object':object})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request,pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content')
    success_url = reverse_lazy('list')

