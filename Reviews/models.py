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
    ("Review","Review"),
)
RATINGS_CHOICES = [(int(i),int(i)) for i in range(0, 101, 5)]
class Category(models.Model):
    category = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category
class ReviewPost(models.Model):
    #Class for review posts
    #CharField for title, not null
    #textfield w/ line breaks for article, not null
    title = models.CharField(max_length=100, unique=True) # post title
    body = models.TextField() #post content
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='review_posts') #Post written by
    created = models.DateField(default=date.today, verbose_name="Date Created", help_text="YYYY-MM-DD") #post date
    updated = models.DateField(auto_now=True, null=True, verbose_name="Date Updated") #post update date
    type = models.CharField(choices=TYPE, default="Review", max_length=10, editable=False) #Type of post has to be blog, cannot be edited
    TopPost = models.BooleanField(default=False, verbose_name="Top Post")
    image = models.ImageField(upload_to='images/', null=True) #Image for post
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Draft/Publish")
    slug = models.CharField(max_length=100, unique=True)
    category_1 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryone", null=True)
    category_1_rating = models.IntegerField(choices=RATINGS_CHOICES)
    category_2 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categorytwo", null=True)
    category_2_rating = models.IntegerField(choices=RATINGS_CHOICES)
    category_3 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categorythree", null=True)
    category_3_rating = models.IntegerField(choices=RATINGS_CHOICES)
    category_4 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryfour", null=True)
    category_4_rating = models.IntegerField(choices=RATINGS_CHOICES)
    overall = models.IntegerField(blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reviewpost_like', blank=True, editable=False)

    class Meta:
        ordering = ['-created']
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
    def overall_score(self):
        return int((self.category_2_rating + self.category_3_rating + self.category_1_rating + self.category_4_rating) / 4)
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("reviewpost", kwargs={"slug": str(self.slug)})
    def save(self, *args, **kwargs):
        self.overall=self.overall_score()
        super(ReviewPost, self).save(*args, **kwargs)

class ReviewComment(models.Model):
    #Class for comments on blog posts
    post = models.ForeignKey(ReviewPost,on_delete=models.CASCADE,related_name='review_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='review_comments')
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
    def __str__(self):
        return 'Comment "{}" by {}'.format(self.body, self.author)
