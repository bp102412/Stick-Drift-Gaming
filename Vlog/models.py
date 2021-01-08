from django.db import models
from datetime import date
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
TYPE = (
    ("Vlog","Vlog"),
)
class VlogPost(models.Model):
    title = models.CharField(max_length = 50)
    video = models.FileField(upload_to='videos/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='vlog_posts') #Post written by
    description = models.TextField()
    created = models.DateField(default=date.today, verbose_name="Date Created", help_text="YYYY-MM-DD")
    updated = models.DateField(auto_now=True, verbose_name="Last Updated")
    top_post = models.BooleanField(default=False, verbose_name="Top Post")
    type = models.CharField(choices=TYPE, default="Vlog", max_length=10, editable=False) #Type of post has to be blog, cannot be edited
    status = models.IntegerField(choices=STATUS,verbose_name="Draft/Publish")
    slug = models.CharField(max_length=100, unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='vlogpost_like', blank=True, editable=False)
    class Meta:
        ordering = ['-created']
        verbose_name = _("Vlog Post")
        verbose_name_plural = _("Posts")
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("vlogpost", kwargs={"slug": str(self.slug)})

class VlogComment(models.Model):
    #Class for comments on blog posts
    post = models.ForeignKey(VlogPost,on_delete=models.CASCADE,related_name='vlog_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='vlog_comments')
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Vlog Comment")
        verbose_name_plural = _("Comments")
    def __str__(self):
        return 'Comment "{}" by {}'.format(self.body, self.author)
