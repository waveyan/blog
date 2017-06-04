from django.shortcuts import render
from .models import Post,Category

def index(request):
    categories=Category.objects.all()
    #template在static文件夹中作参考
    return render(request,'blogapp/index.html',{'categories':categories})

#pk要与urls.py中的url表达式匹配，即要同名
def detail(request,pk):
    post=Post.objects.get(pk=pk)
    categories=Category.objects.all()
    return render(request,'blogapp/detail.html',{'post':post,'categories':categories})

