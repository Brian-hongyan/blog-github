from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_page', kwargs={'pk': self.pk})



# Create your models here.
