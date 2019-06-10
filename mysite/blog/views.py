from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


# Create your views here.
def post_list(request):
    '''
        fetches all published posts and renders them to the user
    '''
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts per page
    page = request.GET.get('page')
    
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/post/list.html',
    {'page': page})


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
