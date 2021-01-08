from django.db import models
from django.conf import settings
from Blog.models import BlogPost
from Vlog.models import VlogPost
from Reviews.models import ReviewPost
# Create your models here.
class Visited(models.Model):
    #Class for comments on blog posts
    blogpost = models.ForeignKey(BlogPost, null=True, on_delete = models.CASCADE, related_name='blogpost_visited')
    vlogpost = models.ForeignKey(BlogPost, null=True, on_delete = models.CASCADE, related_name='blogpost_visited')
    reviewpost = models.ForeignKey(BlogPost, null=True, on_delete = models.CASCADE, related_name='blogpost_visited')
    #newspost = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name='blogpost_visited')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='user_visiting')

class Tag(models.Model):
    tag = models.CharField(max_length=50, help_text="One word descriptors applicable to post.")
