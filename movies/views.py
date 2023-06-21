from django.shortcuts import render
from django.views.generic import ListView, DetailView
from log.models import Post

# Create your views here.
# class PostList(ListView):
#     model = Post
#     ordering = '-pk'

def post_list(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'movies/post_list.html',
        {
            'posts': posts,
        }
    )

# class PostDetail(DetailView):
#     model = Post

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'movies/post_detail.html',
        {
            'post': post,
        }
    )
