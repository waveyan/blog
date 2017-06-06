from django.shortcuts import render
from .models import Post,Category
from comments.forms import CommentForm

def index(request):
    categories=Category.objects.all()
    posts=Post.objects.all()[:6]
    context={'categories':categories,'posts':posts}
    #template在static文件夹中作参考
    return render(request,'blogapp/index.html',context)

#pk要与urls.py中的url表达式匹配，即要同名
def detail(request,pk):
    commentform=CommentForm()
    post=Post.objects.get(pk=pk)
    posts=Post.objects.all()[:6]
    categories=Category.objects.all()
    comments=post.comment_set.all()
    context={'post':post,'categories':categories,'comments':comments,'commentform':commentform,'posts':posts}
    return render(request,'blogapp/detail.html',context)

