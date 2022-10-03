from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
首先命令行输入python manage.py createsuperuser来创建项目的账号和密码
命令行输入python manage.py startapp blog_web，创建新app
创建新app后，需要在mysite文件夹里的settings.py中的INSTALLED_APPS列表里加入app的名字
命令行输入python manage.py runserver，进入主界面
改动了 model.py的内容之后命令行输入python manage.py makemigrations，相当于在该app下建立migrations目录，并记录下你所有的关于models.py的改动，但是这个改动还没有作用到数据库文件
在 makemigrations之后执行命令：python manage.py migrate，将该改动作用到数据库文件，比如产生table，修改字段的类型等。在新创建的项目里也要提前输入
'''


STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):  # models.Model is used to containe a field of data
    title = models.CharField(max_length=200)
    content = models.TextField()
    data_created = models.DateTimeField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return self.title
