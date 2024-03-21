from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Article(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='author')
    headline = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="article")
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    articlemanager = ArticleManager()  # custom manager

    def __str__(self):
        return self.headline
