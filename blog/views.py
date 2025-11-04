from django.shortcuts import render
from django.urls import reverse
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,PermissionRequiredMixin , UpdateView):
    model = Post
    fields = ['title', 'body']
    permission_required = "blog.change_post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def has_permission(self):
        post = self.get_object()
        return super().has_permission() or self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = "blog.delete_post"

    def get_success_url(self):
        return reverse('blog-home')

    def has_permission(self):
        post = self.get_object()
        return super().has_permission() or self.request.user == post.author

def contact_us(request):
    return render(request, "blog/contact_us.html")

