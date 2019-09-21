from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from BookApp.models import Book

def index(request):
    booklist =Book.objects.all()
    # return HttpResponse("<h1>图书管理系统</h1>")
    return render(request,'book/index.html',{'booklist':booklist})
def detail(request,id):
    book =Book.objects.get(pk=id)
    book.views +=1
    book.save()
    return render(request,'book/detail.html',{'book':book})
    # return HttpResponse("图书管理详情页信息 %s" % id)
