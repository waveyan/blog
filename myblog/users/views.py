from django.shortcuts import render,redirect
from .forms import RegisterForm

def regester(request):
    if request.method=='POST':
        registerform=RegisterForm(request.POST)
        #这里如果不通过。这个form会带有错误提示信息
        if registerform.is_valid():
            registerform.save()
            #回到首页
            return redirect('/')
    else:
        registerform=RegisterForm()
    return render(request,'blogapp/register.html',context={'registerform':registerform})
