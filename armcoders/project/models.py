from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="Կատեգորիայի Անուն")
    img = models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200,verbose_name="Փոստի անվանում")
    img = models.ImageField(upload_to="static/images",verbose_name="Փոստի նկար")
    img_1 = models.ImageField(upload_to="static/images",verbose_name="Փոստի փոքր նկարները")
    category = models.ForeignKey(Category,verbose_name="Փոստի կատեգորիան",on_delete=models.CASCADE)
    about = models.CharField(max_length=250, verbose_name="Փոստի մասին հակիրճ")
    about_detail = models.TextField(verbose_name="Փոստի մասին Ընդարձակ")
    link = models.FileField(upload_to="static/files")
    date = models.DateField(auto_now_add=True)
    view = models.IntegerField()


class Comment(models.Model):
    name = models.CharField(max_length=200,verbose_name="մեկնաբանության անուն")
    comment = models.TextField(verbose_name="մեկնաբանություն")
    postId = models.IntegerField()
