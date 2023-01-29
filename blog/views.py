from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
  return render(request, 'blog/index.html', {"posts": posts})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, "blog/post-detail.html", {"post": post})

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])