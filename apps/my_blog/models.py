from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=100)


class Post(models.Model):
    """文章"""
    # 名字
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()
    # 创建时间
    create_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 关联分类, 一个分类对应多个文章
    category = models.ForeignKey(Category)
    # 关联标签, 一个文章可拥有多个标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 关联作者, 一个作者有多篇文章
    author = models.ForeignKey(User)
