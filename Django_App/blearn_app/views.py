from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView,  DeleteView, View

from blearn_app.models import Content
from .forms import ContentForm

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
            return  redirect('signup')
    return render(request,'login.html', {})


def logoutfunc(request):
    logout(request)
    return redirect('login')


class ContentCreate(CreateView):
    model = Content
    template_name = 'create.html'
    form_class = ContentForm
    success_url = reverse_lazy('create')

    # 投稿者ユーザーとリクエストユーザーを紐付ける
    def form_valid(self, form):
        if 'btn_create' in self.request.POST:

            form.instance.user = self.request.user
            return super().form_valid(form)
    
        elif 'btn_replace' in self.request.POST:
            
            # form.is_valid
            data = form.cleaned_data
            title = data['title']
            blur_word = data['blur_word']
            content = data['content']
            # new_content = data['new_content']
            blur_content = content.replace(blur_word, 'xxx')
            # new_content = copy.deepcopy(blur_content)
            # new_content = data[blur_content]
            ctxt = self.get_context_data(blur_content=blur_content, form=form)
            n_content = Content(content=content, title=title, new_content=blur_content, blur_word=blur_word,user=self.request.user,category=data['category'])
            n_content.save()
        return self.render_to_response(ctxt)
        # return self.render(ctxt, 'create.html')
    
    
            # ContentForm
            # new_content.save()

            


    def get_form_kwargs(self, *args, **kwargs):
        kwgs = super().get_form_kwargs(*args, **kwargs)
        category_choice = ((1, "network"), (2, "web"), (3, "linux"),(4, "git"))
        kwgs["categories"] = category_choice
        return kwgs
    
class Index(View):
    form_class = ContentForm



class ContentList(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = Content
    # model2 = Category
    
    def get_queryset(self):
        return Content.objects.filter(user=self.request.user,category="1")

    
class ContentList2(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = Content

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user,category="2")
    
    
class ContentList3(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = Content

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user,category="3")
    
    
class ContentList4(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = Content

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user,category="4")
    

class ContentDetail(DetailView):
    template_name = 'detail.html'
    model = Content
    
    
    def __str__(self):
        content = Content.content
        blur_word = Content.blur_word
        new_content = content.replace(blur_word,'----')
        new_content = Content.new_content
        
        # return render('detail.html',new_content=new_content)
        ctxt = self.get_context_data(new_content=new_content)
        return self.render_to_response(ctxt)
        
    
    
        
    

    # 詳細画面でcontentの中にblur_wordと一致するものがあれば、blurをかける
    # def get_queryset(self):
        
    #     match_word = Content.objects.filter('blur_word' == 'content')
    #     return match_word



    # blur_wordの中の単語とcontentの中の文章を比較して、blur_wordに一致する単語にのみblurをかける
    # def get_queryset(self):
    #     Content.objects.filter

# class ContentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     template_name = 'update.html'
#     # fieldに入っているデータをModelから持ってくるのに必要
#     model = Content
#     form_class = ContentForm

#     def get_success_url(self, **kwargs):
#         '''編集完了後の遷移先'''
#         pk = self.kwargs["pk"]
#         return reverse_lazy('detail', kwargs={"pk":pk})

#     def test_func(self, **kwargs):
#         '''アクセスできるユーザーを制限'''
#         pk = self.kwargs["pk"]
#         post = Content.objects.get(pk=pk)
#         return (post.user == self.request.user)

class ContentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''投稿削除ページ'''
    model = Content
    template_name = 'delete.html'
    success_url = reverse_lazy('create')

    def test_func(self, **kwargs):
        '''アクセスできるユーザーを制限'''
        pk = self.kwargs["pk"]
        post = Content.objects.get(pk=pk)
        return (post.user == self.request.user)

        # 表示するfieldをHTML上で決める