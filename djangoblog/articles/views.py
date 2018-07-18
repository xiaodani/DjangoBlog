from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles' : articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'articles/article_detail.html', {'article' : article})

@login_required(login_url= "/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form' : form})
