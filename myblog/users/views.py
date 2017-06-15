from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

def regester(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        #这里如果不通过。这个form会带有错误提示信息
        if form.is_valid():
            form.save()
            #回到首页
            return redirect('/')
    else:
        form=RegisterForm()
        return render(request,'blogapp/signin_or_signout.html',context={'form':form,'title':'注册','action_url':reverse('users:register')})

#不能与login同名
def signin(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        #在url的参数获取都是GET
        next_to=request.GET.get('next_to')
        print(next_to)
        if form.is_valid():
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(next_to or '/')
            else:
                messages.error(request,'用户名或密码不正确')
                return redirect(reverse('users:login')+'?next_to=%s'%next_to)
    else:
        form=LoginForm()
        register_html='还没有账户？点击<a href="%s">这里</a>加入我们。'%(reverse('users:register'))
        action_url=reverse('users:login')
        context={'form':form,'title':'登录','register_html':register_html,'action_url':action_url}
        return render(request,'blogapp/signin_or_signout.html',context=context)

def signout(request):
    logout(request)
    return redirect('/')

