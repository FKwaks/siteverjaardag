from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'profiel/', default = 'media/profile.png')
    naam = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    relatie = models.CharField(max_length = 100)
    text = models.TextField()
    completed_date = models.DateTimeField(
            blank=True, null=True)
    completed = False

    def publish(self):
        self.completed_date = timezone.now()
        self.completed = True
        self.save()

    def __str__(self):
        return self.naam
