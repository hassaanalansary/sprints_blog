from django.urls import path
from .views import contact_us
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path("", PostListView.as_view(), name= 'blog-home'),
    path("contact-us/", contact_us, name='contact-us'),
    path("new/", PostCreateView.as_view(), name='post-create'),
    path("<str:slug>/update/", PostUpdateView.as_view(), name='post-update'),
    path("<str:slug>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("<str:slug>/", PostDetailView.as_view(), name="blog-post"),
]
