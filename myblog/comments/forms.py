from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        #根据model中定义的字段类型生成表单
        fields=['text']
        #改变表单属性
        widgets={
            'text':forms.Textarea(attrs={'class':'from-control'})
        }





