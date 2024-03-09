from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    introduction = models.TextField()
    tags = models.ManyToManyField('Tag', through = 'AddTag')
    image = models.ImageField(upload_to='games/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Character(models.Model):
    name = models.CharField(max_length=200)
    storyline = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name = 'characters', blank=True, null=True)
    image = models.ImageField(upload_to='characters/', null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AddTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return " "


    
class Rating(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Rating: {self.score}"

class Comment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment: {self.text}"