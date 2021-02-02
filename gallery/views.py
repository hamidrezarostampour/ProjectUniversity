from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from .models import Post, Comment

#from django.shortcuts import render

# Create your views here.


#def home(request):
#    return render(request, 'gallery/home.html')


class PostList(ListView):
    model = Post
    paginate_by = 9
    ordering = ['-created']


class PostDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)



#@login_required
def like_or_dislike(request, pk):
    # print(request.resolver_match)
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    post_likes_users = post.likes.all()
    count = post_likes_users.count()

    if user.is_anonymous:
        return JsonResponse({
            'likes': count,
            'status': 'not_login',
        })

    if user in post_likes_users:
        post.likes.remove(user)
        count -= 1
        user_in_likes = False
    else:
        post.likes.add(user)
        count += 1
        user_in_likes = True

    return JsonResponse({
        'status': user.is_authenticated,
        'likes': count,
        'user_in_likes': user_in_likes,
    })


def comment(request, pk):
    # print(request.resolver_match)
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    
    
    if user.is_anonymous:
        return JsonResponse({
            'status': 'not_login',
        })
    content = request.POST.get('content')
    if content == '':
        return JsonResponse({
            'status': 'bad_content',
        })
    Comment.objects.create(
        user = user,
        post = post,
        content = content
    )
    post_comments = post.comments.all()
    count = post_comments.count()
    
    all_comments = []
    for cmmnt in post_comments:
        all_comments.append({'created': cmmnt.created_date, 'username': cmmnt.user.username, 'content': cmmnt.content})
    

    return JsonResponse({
        'status': user.is_authenticated,
        'count': count,
        'user': user.username,
        'post_comments': all_comments
    })