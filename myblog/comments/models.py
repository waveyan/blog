from django.db import models

class Comment(models.Model):
    ip=models.CharField('ip地址',max_length=15)
    city=models.CharField('所在地',max_length=20)
    text=models.TextField()
    #自动把值设置为当前时间
    created_time=models.DateTimeField('评论时间',auto_now_add=True)
    #引用其他应用的model
    post=models.ForeignKey('blogapp.Post')

    def __str__(self):
        return self.ip+':'+self.city+':'+self.text

    class Meta:
        ordering=['-created_time']



