from django.shortcuts import render
from Blog.models import BlogPost
from Vlog.models import VlogPost
from Reviews.models import ReviewPost
from itertools import chain
from operator import attrgetter
from datetime import date
# Create your views here.
def home(request):
    posts = sorted(list(chain(BlogPost.objects.filter(status=1).filter(TopPost=1).order_by('-created'), VlogPost.objects.filter(status=1).filter(top_post=1).order_by('-created'), ReviewPost.objects.filter(status=1).filter(TopPost=1).order_by('-created'))),key=attrgetter('created')) # all top posts
    posts.reverse()
    if posts:
        featured = posts[0] # newest top post
    else:
        featured = 0
    posts = sorted(list(chain(BlogPost.objects.filter(status=1).order_by('-created'), VlogPost.objects.filter(status=1).order_by('-created'),ReviewPost.objects.filter(status=1).order_by('-created'))),key=attrgetter('created'))
    posts.reverse()
    if featured == 0:
        featured = posts[0]
    try:
        posts.pop(posts.index(featured))
    except IndexError:
        pass
    blogPosts = BlogPost.objects.filter(status=1).order_by('-created')  #all blog posts
    vlogPosts = VlogPost.objects.filter(status=1).order_by('-created')  #all vlog posts
    reviewPosts = ReviewPost.objects.filter(status=1).order_by('-created')

    return render(request, 'index.html', {"Featured":featured,'Posts':posts, 'Blog':blogPosts, 'Vlog':vlogPosts, 'Review':reviewPosts,})
