from django.urls import path
from .views import blog_home, contact_us, blog_season, blog_season_by_number
urlpatterns = [
    path("", blog_home, name= 'blog-home'),
    path("contact-us/", contact_us, name='contact-us'),
    path("<int:season>/", blog_season_by_number, name='blog-season-by-number'),
    path("<str:season>/", blog_season, name="blog-season"),
]
