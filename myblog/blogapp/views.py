from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comments.forms import CommentForm
from django.db.models.aggregates import Count

def index(request):
    categories=Category.objects.annotate(post_num=Count('post')).all()
    posts=Post.objects.all()[:6]
    post=Post.objects.order_by('-read').first()
    context={'categories':categories,'posts':posts,'post':post}
    #template在static文件夹中作参考
    return render(request,'blogapp/index.html',context)

#pk要与urls.py中的url表达式匹配，即要同名
def detail(request,pk):
    commentform=CommentForm()
    post=Post.objects.annotate(comment_num=Count('comment')).get(pk=pk)
    #增1阅读量
    post.increase_read()
    posts=Post.objects.all()[:6]
    #增1阅读量
    categories=Category.objects.all()
    comments=post.comment_set.all()
    context={'post':post,'categories':categories,'comments':comments,'commentform':commentform,'posts':posts}
    return render(request,'blogapp/detail.html',context)

def posts(request):
    posts=Post.objects.annotate(comment_num=Count('comment')).all()
    context={'posts':posts}
    categories=Category.objects.annotate(post_num=Count('post')).all()
    context={'categories':categories,'posts':posts}
    return render(request,'blogapp/posts.html',context)

def get_posts_with_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    categories=Category.objects.annotate(post_num=Count('post')).all()
    context={'categories':categories,'posts':category.post_set.all()}
    return render(request,'blogapp/posts.html',context)



