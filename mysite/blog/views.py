from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


# Create your views here.
class PostListView(ListView):
    '''
        fetches all published posts and renders them to the user
    '''
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name='blog/post/list.html'
    paginate_by = 3    


def post_detail(request, year, month, day, post):
    '''
        fetches a particular post and renders it to user
    '''
    post = get_object_or_404(Post, slug=post,
    status='published', publish__year=year,
    publish__month=month, publish__day=day)
    
    return render(request, 'blog/post/detail.html', {
        'post': post
    })
