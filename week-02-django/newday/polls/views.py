from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello! it's yesterday!")
    # name = "minnie"
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title="hello",
    #     contents="this is test",
    #     view_count=0
    # )
    ctx={
        "article_list":article_list
    }
    return render(request, "index.html", ctx )
    # return HttpResponse(article.title)
