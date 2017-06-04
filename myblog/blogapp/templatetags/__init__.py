'''
1.在应用目录下创建templatetags文件夹，并在文件夹中创建__init__.py,为一个py包
2.在templatetags文件夹下创建一个py文件，用来写标签代码和注册标签代码，如myblog_tag,py,名字没有规定
3.在.py文件中输入：
from django import template
register=template.Library()
用@register。simple_tag装饰标签函数（函数名与自定义标签名一样）
4.在某个模版中使用自定义标签
{%load 那个.py文件名%}即可使用自定义标签
'''
