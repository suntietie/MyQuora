from django.db import models
from django.conf import settings


# Create your models here.
class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content = models.CharField(max_length=240)
    # A Slug is basically a short label for something, containing only letters, numbers, underscores or hyphens.
    # create slug based on the content 
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="questions")
    
    def __repr__(self):
        self.content

class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    body = models.TextField()
    question = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name="answers")

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")
    
    def __repr__(self):
        return self.author
