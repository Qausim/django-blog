from django.shortcuts import get_object_or_404, render


from .models import Post

# Create your views here.
def post_list(request):
    '''
        fetches all published posts and renders them to the user
    '''
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {
        'posts': posts
    })


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