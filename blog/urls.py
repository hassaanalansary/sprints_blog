from django.urls import path
from .views import blog_home, contact_us, blog_post, blog_post_by_number
urlpatterns = [
    path("", blog_home, name= 'blog-home'),
    path("contact-us/", contact_us, name='contact-us'),
    path("<int:post_id>/", blog_post_by_number, name='blog-post-by-number'),
    path("<str:slug>/", blog_post, name="blog-post"),
]
