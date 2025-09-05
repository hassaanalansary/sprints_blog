from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from blog.models import Post

def blog_home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", context={"posts": posts})

def contact_us(request):
    return render(request, "blog/contact_us.html")


def blog_post(request, slug: str):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404()
    
    return render(request, "blog/post.html", context={"post": post})

def blog_post_by_number(request, post_id:int):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404()

    return redirect("blog-post" , slug = post.slug)
