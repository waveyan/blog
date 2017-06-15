from django.shortcuts import render,get_object_or_404,redirect
from blogapp.models import Post
from django.contrib.auth.decorators import login_required

from .models import Comment
from .forms import CommentForm

import requests
import json


#non-default argument follows default argument
def get_location_by_ip(ip,key='e63459d9c421f2f67fda5dacaa037a48'):
    url='http://restapi.amap.com/v3/ip?key=%s&ip=%s&output=JSON'%(key,ip)
    s=requests.session()
    data=s.get(url)
    position_dict=json.loads(data.text)
    return ''.join(position_dict.get('province'))+''.join(position_dict.get('city'))

#redirect_field_name是?后面的属性,默认为next
@login_required(login_url='/login',redirect_field_name='next_to')
def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    if request.method=='POST':
        #request.POST一个类字典对象，存有表单的值
        #创建一个有值得Form对象
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            #获取客户ip
            ip=request.META.get('REMOTE_ADDR')
            #commit=False不提交数据库，生成comment Model实例
            #为了和post关联
            comment=commentform.save(commit=False)
            comment.post=post
            comment.city=get_location_by_ip(ip)
            comment.ip=ip
            comment.save()
            #redirect会重定向到get_absolute_url方法返回的url
            return redirect(post)
        else:
            #为了错误信息提示
            comments=post.comment_set.all()
            context={'post':post,'commentform':commentform,'comments':comments}
            return render(request,'blogapp/detail.html',context)
    else:
        return redirect(post)

