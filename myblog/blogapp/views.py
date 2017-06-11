from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comments.forms import CommentForm
from django.db.models.aggregates import Count
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myblog.settings import PER_PAGE

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

#功能与detail一致
class PostDetailView(DetailView):
    model=Post
    template_name='blogapp/detail.html'
    context_object_name='post'

   # #重写,这是DetailView最后调用的,会调用其他DetailView的内置函数
   # def get(self,request,*args,**kwargs):
   #     #调用父类的get DetailView才会根据url的pk,调用get_object找到相应的post,即self.object
   #     response=super().get(self,request,*args,**kwargs)
   #     #阅读量
   #     self.object.increase_read()
   #     print(response)
   #     #返回一个HttpResponse
   #     return response

    def get_object(self,queryset=None):
        #post=super().get_object(queryset=None)
        post=Post.objects.annotate(comment_num=Count('comment')).get(pk=self.kwargs.get('pk'))
        post.increase_read()
        return post

    #重写，也会自动被get调用
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        posts=Post.objects.all()[:6]
        categories=Category.objects.all()
        #self.kwargs与参数的kwargs不是同一个
        comments=Post.objects.get(pk=self.kwargs.get('pk')).comment_set.all()
        commentform=CommentForm()
        #post自动了
        context.update({
            'categories':categories,
            'comments':comments,
            'commentform':commentform,
            'posts':posts,
        })
        return context





def posts(request):
    posts_list=Post.objects.annotate(comment_num=Count('comment')).all()
    #分页：每页pages篇
    paginator=Paginator(posts_list,PER_PAGE)
    page=request.GET.get('page')
    try:
        p=paginator.page(page)
    except PageNotAnInteger:
        p=paginator.page(1)
    except Emptypage:
        p=paginator.page(paginator.num_pages)
    is_paginated=lambda:paginator.num_pages>1
    categories=Category.objects.annotate(post_num=Count('post')).all()
    context={'categories':categories,'posts':p.object_list,'is_paginated':is_paginated,'page_obj':p,'paginator':paginator}
    return render(request,'blogapp/posts.html',context)

def get_posts_with_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    categories=Category.objects.annotate(post_num=Count('post')).all()
    context={'categories':categories,'posts':category.post_set.all()}
    return render(request,'blogapp/posts.html',context)

#使用类视图,功能与get_post_with_category一致
class CategoryView(ListView):
    #需要获取post的列表
    model=Post
    template_name='blogapp/posts.html'
    #post列表在context的name
    context_object_name='posts'
    #每页数量，已向模版传递了paginator、page_obj、is_paginated、object_list参数
    paginate_by=PER_PAGE

    #重写get_queryset,表示如何获取这个posts列表
    def get_queryset(self):
        #获取url上的pk
        category=get_object_or_404(Category,pk=self.kwargs.get('pk'))
        #return super().get_queryset().filter(category=category)
        return Post.objects.annotate(comment_num=Count('comment')).filter(category=category)

    #重写get_contxt_data
    def get_context_data(self,**kwargs):
        #先获取posts list，即调用了get_queryset
        #post list交由ListView获取了，我自己获取categories
        context=super().get_context_data(**kwargs)
        categories=Category.objects.annotate(post_num=Count('post')).all()
        context.update({'categories':categories,'cate':'i am category'})
        return context























