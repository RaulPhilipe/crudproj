from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    score = models.CharField(max_length=11)
    genre = models.CharField(max_length=100)
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='movie')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "movie"
    