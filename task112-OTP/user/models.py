from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class PostCrud(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.owner} , {self.slug}, {self.title} , {self.text}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostCrud, self).save(*args, **kwargs)
