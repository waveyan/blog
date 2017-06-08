from django.db import models
#Django内置应用，专门用于处理网站用户的注册、登陆等流程。
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#文章类别，id不写，自动生成,默认为主键
class Category(models.Model):
    name=models.CharField('类别',max_length=100)

    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name=models.CharField('标签',max_length=100)

    def __str__(self):
        return self.name


#文章
class Post(models.Model):
    #自定义方法使用methodname.short_description='xxx',字段传入第一个参数为别名即可在admin中显示
    title=models.CharField('题目',max_length=70)
    body=models.TextField('文章')
    created_time=models.DateTimeField('创作时间')
    modified_time=models.DateTimeField('最后修改时间',auto_now_add=True)
    #摘要blank=True,允许空值
    excerpt=models.CharField('摘要',max_length=200,blank=True)
    #这里赋值时直接用Category对象初始化
    category=models.ForeignKey(Category)
    #
    tags=models.ManyToManyField(Tag,blank=True)
    #作者使用内置User，直接用User对象初始化,User即系登陆admin的user，管理员
    author=models.ForeignKey(User)
    #admin管理会自动存于django的settings.py文件中定义的变量MEDIA_ROOT路径下
    pic=models.FileField(blank=True)
    #访问数量,只允许正整数或0
    read=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''相当于url_for,自带pk,kwargs可随意，只要是dict就可以'''
        return reverse('blogapp:detail',kwargs={'pk':self.pk})

    def increase_read(self):
        self.read+=1
        #只更新read字段
        self.save(update_fields=['read'])

    #用在posts.html的目录循环出来的post中
    #def comment_num(self):
    #    return len(self.comment_set.all())

    def save(self,*args,**kwargs):
        '''自动生成摘要，取正文前50字'''
        self.excerpt=self.body[:50]
        super().save(*args,**kwargs)

    #python类有继承需要带括号，没有括号默认继承object类
    class Meta:
        '''指定默认的排序属性,Post.objects.all()时效果等同Post.objects.all().order_by('-created_time')'''
        ordering=['-created_time','title']




class Url(models.Model):
    name=models.CharField('url名称',max_length=100)
    url=models.CharField('url',max_length=200)
    created_time=models.DateTimeField('录入时间')

    def __str__(self):
        return self.name


class Sentence(models.Model):
    sentence=models.TextField('美句',max_length=500)
    created_time=models.DateTimeField('收入时间')
    originate_from=models.CharField('出自',max_length=50,blank=True)

    def __str__(self):
        return self.sentence


