from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

#Post can be a draft or published
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
#Post Type has to be blog. Only present for the Type label in template
TYPE = (
    ("Blog","Blog"),
)

class BlogPost(models.Model):
    #Class for blog posts
    #CharField for title, not null
    #textfield w/ line breaks for article, not null
    title = models.CharField(max_length=100, unique=True) # post title
    body = models.TextField() #post content
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='blog_posts') #Post written by
    created = models.DateField(default=date.today, verbose_name="Date Created", help_text="YYYY-MM-DD") #post date
    updated = models.DateField(auto_now=True, null=True, verbose_name="Date Updated") #post update date
    type = models.CharField(choices=TYPE, default="Blog", max_length=10, editable=False) #Type of post has to be blog, cannot be edited
    TopPost = models.BooleanField(default=False, verbose_name="Top Post")
    image = models.ImageField(upload_to='images/', null=True) #Image for post
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Draft/Publish")
    slug = models.CharField(max_length=100, unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blogpost_like', blank=True, editable=False)
    # add likes
    # add updated content, null = True
    # add featured option for updated posts to reinclude on home page, null =True
    class Meta:
        ordering = ['-created']
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Posts")

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blogpost", kwargs={"slug": str(self.slug)})

class BlogComment(models.Model):
    #Class for comments on blog posts
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='blog_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='blog_comments')
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
    def __str__(self):
        return 'Comment "{}" by {}'.format(self.body, self.author)
