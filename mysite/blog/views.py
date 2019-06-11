from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import EmailPostForm
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


def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f'{data["name"]} ({data["email"]}) recommends you reading "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n{data["name"]}\'s comments: {data["comments"]}.'
            send_mail(subject, message, 'admin@myblog.com', [data['to']])
            
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })
