from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE) #IF THE USER IS DELTED ALL HIS POSTS WILL BE DELETED , USE "CASCADE"

    def __str__(self):
        return '<Author:{} , ID:{}>, Title:{}'.format(self.author, self.id, self.title)