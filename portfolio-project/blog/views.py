from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    data_dict = dict(blogs=blogs)
    return render(request, 'blog/blogs.html', data_dict)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    data_dict = dict(blog=blog)
    return render(request, 'blog/blog.html', data_dict)
