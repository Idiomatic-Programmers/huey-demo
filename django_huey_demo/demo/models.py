from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.word