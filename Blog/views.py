from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def blog(request):
    blogPosts = BlogPost.objects.filter(status=1).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(blogPosts, 10)
    page_obj = paginator.get_page(page)
    return render(request, 'blog.html', {'posts':blogPosts,'page_obj': page_obj,})

def post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.blog_comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    postLiked=False
    if post.likes.filter(id=request.user.id).exists():
        postLiked = True
    numLikes = post.number_of_likes()
    return render(request, 'blog-post.html', {'liked':postLiked, 'likes':numLikes, 'post':post,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form,})

def like(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost', args=[str(slug)]))
